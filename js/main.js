(function(){
var b=document.getElementById('burger'),m=document.getElementById('menu');
function set(o){m.classList.toggle('open',o);b.setAttribute('aria-expanded',o);b.setAttribute('aria-label',o?'Fermer le menu':'Ouvrir le menu')}
b.addEventListener('click',function(){set(!m.classList.contains('open'))});
m.addEventListener('click',function(e){if(e.target.closest('a'))set(false)});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&m.classList.contains('open')){set(false);b.focus()}});
function copyText(t,btn){
  var done=function(l){var o=btn.dataset.l||btn.textContent;btn.dataset.l=o;btn.textContent=l;setTimeout(function(){btn.textContent=o},1800)};
  if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(function(){done('Copié')},function(){fb()})}else fb();
  function fb(){var ta=document.createElement('textarea');ta.value=t;document.body.appendChild(ta);ta.select();try{document.execCommand('copy');done('Copié')}catch(e){done('Sélectionnez le texte')}ta.remove()}
}
document.querySelectorAll('.copy').forEach(function(btn){btn.addEventListener('click',function(){copyText(document.getElementById(btn.dataset.copy).textContent,btn)})});
var f=document.getElementById('contact-form');
if(f){
  var TEL='+33624363376',MAIL='contact@albizzia-paysage.com';
  var rules={
    nom:function(v){return v.trim().length>=2?'':'Indiquez votre nom.'},
    tel:function(v){return /^(?:(?:\+|00)33|0)[1-9](?:[\s.\-]?\d{2}){4}$/.test(v.trim())?'':'Saisissez un numéro français valide, par exemple 06 12 34 56 78.'},
    email:function(v){return v.trim()===''||/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim())?'':'Saisissez une adresse e-mail valide, par exemple nom@exemple.fr.'},
    commune:function(v){return v.trim().length>=2?'':'Indiquez la commune du chantier.'},
    prestation:function(v){return v?'':'Choisissez une prestation.'},
    message:function(v){return v.trim().length>=10?'':'Décrivez votre projet en quelques mots (10 caractères minimum).'}
  };
  function check(id){var el=document.getElementById(id),msg=rules[id](el.value),er=document.getElementById('err-'+id);er.textContent=msg;el.setAttribute('aria-invalid',msg?'true':'false');return !msg}
  Object.keys(rules).forEach(function(id){document.getElementById(id).addEventListener('blur',function(){check(id)})});
  f.addEventListener('submit',function(e){
    e.preventDefault();
    var bad=Object.keys(rules).filter(function(id){return !check(id)});
    if(bad.length){document.getElementById(bad[0]).focus();return}
    var g=function(id){return document.getElementById(id).value.trim()};
    var txt='Bonjour, je souhaite un devis à Albizzia Paysage.\nPrestation : '+g('prestation')+'\nCommune : '+g('commune')+'\nProjet : '+g('message')+'\nNom : '+g('nom')+'\nTéléphone : '+g('tel')+(g('email')?'\nE-mail : '+g('email'):'')+'\nMerci.';
    document.getElementById('recap-text').textContent=txt;
    document.getElementById('recap-sms').href='sms:'+TEL+'?body='+encodeURIComponent(txt);
    document.getElementById('recap-mail').href='mailto:'+MAIL+'?subject='+encodeURIComponent('Demande de devis - '+g('prestation'))+'&body='+encodeURIComponent(txt);
    var r=document.getElementById('recap');r.hidden=false;r.scrollIntoView({behavior:'smooth',block:'center'});document.getElementById('recap-title').focus();
  });
  document.getElementById('recap-copy').addEventListener('click',function(){copyText(document.getElementById('recap-text').textContent,this)});
}
})();
