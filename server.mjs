import http from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { resolve, extname, sep } from 'node:path';

const root = resolve('dist');
const types = {'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.json':'application/json; charset=utf-8','.svg':'image/svg+xml','.png':'image/png','.pdf':'application/pdf','.woff2':'font/woff2','.xml':'application/xml; charset=utf-8','.txt':'text/plain; charset=utf-8','.bib':'text/plain; charset=utf-8','.md':'text/plain; charset=utf-8'};
http.createServer(async (req,res) => {
  try {
    if (!['GET','HEAD'].includes(req.method)) {res.writeHead(405, {Allow:'GET, HEAD'}); return res.end();}
    const url = new URL(req.url,'http://localhost');
    if (url.pathname === '/healthz') {await stat(resolve(root,'index.html')); res.writeHead(200, {'Content-Type':'application/json'}); return res.end('{"status":"ok","app":"lyrebird"}');}
    const pathname = decodeURIComponent(url.pathname);
    let path = resolve(root, '.' + pathname);
    if (!path.startsWith(root + sep) && path !== root) {res.writeHead(403); return res.end();}
    let status = 200;
    try {
      if ((await stat(path)).isDirectory()) {
        if (!pathname.endsWith('/')) {res.writeHead(308,{Location:pathname+'/'+url.search}); return res.end();}
        path = resolve(path,'index.html');
      }
      await stat(path);
    } catch {status=404; path=resolve(root,'404.html');}
    const body = await readFile(path);
    res.writeHead(status, {'Content-Type':types[extname(path)]||'application/octet-stream','X-Content-Type-Options':'nosniff','Referrer-Policy':'strict-origin-when-cross-origin','X-Frame-Options':'DENY','Content-Security-Policy':"default-src 'self'; style-src 'self'; script-src 'self'; img-src 'self' data:; font-src 'self'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'",'Cache-Control':pathname.startsWith('/assets/')?'public, max-age=3600':'public, max-age=60'});
    res.end(req.method==='HEAD'?undefined:body);
  } catch {res.writeHead(400); res.end('Invalid request');}
}).listen(Number(process.env.PORT||8080),'0.0.0.0',()=>console.log('Lyrebird listening on '+(process.env.PORT||8080)));
