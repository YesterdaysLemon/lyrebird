async (page) => {
  const issues=[];
  const base='http://localhost:8084';
  page.on('pageerror',e=>issues.push(String(e)));
  page.on('console',e=>{if(e.type()==='error')issues.push(e.text());});
  const response=await page.request.get(base+'/catalog.json');
  const papers=await response.json();
  for(const width of [1440,360]){
    await page.setViewportSize({width,height:900});
    for(const path of ['/', '/about/', ...papers.map(p=>'/papers/'+p.slug+'/')]){
      const r=await page.goto(base+path+'?qa='+Date.now());if(r.status()!==200)throw new Error('HTTP '+r.status()+' '+path);
      await page.evaluate(()=>document.fonts.ready);
      const metrics=await page.evaluate(()=>({width:innerWidth,scroll:document.documentElement.scrollWidth,broken:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src)}));
      if(metrics.scroll>width||metrics.broken.length)throw new Error(JSON.stringify({path,width,metrics}));
    }
  }
  await page.goto(base+'/');
  await page.getByRole('searchbox').fill('geometry');
  if(await page.locator('[data-paper]:visible').count()!==1)throw new Error('Search failed');
  await page.getByRole('searchbox').fill('');
  await page.getByRole('combobox').selectOption('Mathematics');
  if(await page.locator('[data-paper]:visible').count()!==1)throw new Error('Topic failed');
  await page.getByRole('searchbox').fill('zzzznosuchpaper');
  if(!await page.getByRole('button',{name:'Clear filters'}).isVisible())throw new Error('Empty state missing');
  await page.getByRole('button',{name:'Clear filters'}).click();
  if(await page.locator('[data-paper]:visible').count()!==papers.length)throw new Error('Reset failed');
  await page.goto(base+'/papers/'+papers[0].slug+'/');
  await page.context().grantPermissions(['clipboard-read','clipboard-write']);
  await page.getByRole('button',{name:'Copy citation'}).click();
  await page.getByRole('button',{name:'Copied ✓'}).waitFor({state:'visible',timeout:5000});
  const clip=await page.evaluate(()=>navigator.clipboard.readText());
  if(!clip.includes(papers[0].title))throw new Error('Wrong citation');
  for(const p of papers){const pdf=await page.request.get(base+'/papers/'+p.slug+'/paper.pdf');if(pdf.status()!==200||(await pdf.body()).subarray(0,5).toString()!=='%PDF-')throw new Error('PDF '+p.slug);}
  if((await page.request.get(base+'/missing-page')).status()!==404)throw new Error('404 failed');
  if(issues.length)throw new Error(JSON.stringify(issues));
  return 'BROWSER_QA_PASS: '+papers.length+' papers; 1440px and 360px; search, topic, reset, clipboard, PDFs, 404; zero errors';
}
