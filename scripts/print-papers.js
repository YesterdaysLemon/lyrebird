async (page) => {
  const slugs = ['learning-what-to-keep','voice-without-a-prescribed-self','heart-wall-sampling','fixed-rate-optimization','ghz-closure'];
  await page.setViewportSize({width:1200,height:900});
  for (const slug of slugs) {
    await page.goto('http://localhost:8084/papers/'+slug+'/?print='+Date.now());
    await page.evaluate(()=>document.fonts.ready);
    await page.pdf({path:'public/papers/'+slug+'/paper.pdf',format:'A4',printBackground:true,displayHeaderFooter:true,margin:{top:'19mm',bottom:'21mm',left:'20mm',right:'20mm'},headerTemplate:'<div></div>',footerTemplate:'<div style="font-size:9px;color:#555;width:100%;margin:0 20mm;display:flex;justify-content:space-between"><span>LYREBIRD · Independent research · Not peer reviewed</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>'});
  }
  console.log('Printed '+slugs.length+' research papers');
}
