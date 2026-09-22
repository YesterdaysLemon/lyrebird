const search=document.querySelector('#search');
const topic=document.querySelector('#topic');
const entries=[...document.querySelectorAll('[data-paper]')];
if(search&&topic){
  const params=new URLSearchParams(location.search);search.value=params.get('q')||'';topic.value=params.get('area')||'';
  const filter=()=>{const query=search.value.trim().toLowerCase();let count=0;for(const entry of entries){entry.hidden=!(query.split(/\s+/).every(word=>entry.dataset.search.includes(word))&&(!topic.value||entry.dataset.topic===topic.value));if(!entry.hidden)count++;}document.querySelector('#result-count').textContent=`${count} ${count===1?'paper or note':'papers and notes'}`;document.querySelector('#empty').hidden=count>0;const p=new URLSearchParams();if(query)p.set('q',search.value);if(topic.value)p.set('area',topic.value);history.replaceState(null,'',location.pathname+(p.size?'?'+p:'')+location.hash);};
  search.addEventListener('input',filter);topic.addEventListener('change',filter);search.closest('form').addEventListener('submit',e=>e.preventDefault());document.querySelector('#reset-filters').addEventListener('click',()=>{search.value='';topic.value='';filter();search.focus();});filter();
}
document.querySelectorAll('[data-cite]').forEach(button=>button.addEventListener('click',async()=>{const status=button.parentElement.querySelector('.copy-status');try{const r=await fetch('citation.bib');if(!r.ok)throw new Error('Citation unavailable');const text=await r.text();await navigator.clipboard.writeText(text);status.textContent='Citation copied.';button.textContent='Copied ✓';}catch{status.textContent='Use the BibTeX download beside this button.';}}));
