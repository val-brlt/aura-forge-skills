'use strict';
// Révision UX R2 : questions structurées, discussion contextuelle et thèmes locaux.
const refBase = {render, reset, renderInterview, renderProposals, showScreen, makeVersion, snapshot, status};
let refQuestionId = 'annulation', refDiscussionId = 'annulation', refAnalysisBusy = false;
const refLocked = () => !project() || project().archived || version().approved || version().delivered || !version().active;
status = function(v){return !v.approved&&!v.delivered&&!v.suspended&&!v.summaryApproved&&!v.catalogueApproved?(v.analysisDone===false?'Idée à analyser':'Questions en cours'):refBase.status(v);};

function refProjectChat(p=project()){
  if(!p.projectChat)p.projectChat=[{author:'assistant',text:`## Parlons de ${p.name}\n\nJe m’appuie sur la description du projet, ses versions et leurs décisions pour vous aider à prendre du recul.\n\nVous pouvez explorer un nouveau besoin, préciser l’objectif du projet ou retrouver le fil de vos réflexions.\n\n**Par quoi souhaitez-vous commencer ?**`}];
  return p.projectChat;
}
function refProjectChatContext(p=project()){
  const v=p.versions.find(v=>v.id===p.selectedVersion),baseline=p.versions.filter(v=>v.approved).at(-1);
  return {version:v.id,approved:v.approved,delivered:v.delivered,state:status(v),baseline:baseline?`${baseline.id}, cadrage approuvé, ${baseline.delivered?'livraison déclarée':'livraison non confirmée'}`:'Aucun cadrage approuvé de référence',description:p.description};
}
function refRenderProjectChat(){
  const p=project();if(!p)return;const context=refProjectChatContext(p);
  $('#project-chat-messages').innerHTML=refProjectChat(p).map(m=>`<article class="message ${m.author==='user'?'user':''}"><strong>${m.author==='user'?'Vous':'Assistant du projet'}</strong><div class="markdown">${refMarkdown(m.text)}</div>${m.contextVersion?`<p class="chat-message-context">Contexte de cet échange : ${esc(m.contextVersion)}</p>`:''}</article>`).join('');
  $('#project-chat-description').textContent=p.description;$('#project-chat-version').textContent=`${context.version} · ${context.state}`;$('#project-chat-baseline').textContent=context.baseline;
  $('#project-chat-input').value=p.projectChatDraft||'';$('#project-chat-loading').hidden=!p.projectChatBusy;$('#project-chat-error').hidden=!p.projectChatError;
  const blocked=p.archived||p.projectChatBusy||p.projectChatError;$('#project-chat-input').disabled=!!blocked;$('#project-chat-send').disabled=!!blocked;$('#project-chat-retry').disabled=p.archived||!!p.projectChatBusy;
}
async function refProjectChatRespond(){
  const p=project();if(!p||p.archived||p.projectChatBusy)return;
  const context=p.projectChatRequest||refProjectChatContext(p),token=generation;p.projectChatBusy=true;p.projectChatError=false;refRenderProjectChat();
  await new Promise(resolve=>setTimeout(resolve,850));if(token!==generation||!projects.includes(p))return;
  refProjectChat(p).push({author:'assistant',contextVersion:context.version,text:`### Repartons du contexte du projet\n\n${context.description}\n\n**Où en est le projet ?**\n\n- Version consultée : **${context.version}**, ${context.state.toLowerCase()}.\n- Référence : ${context.baseline}.\n- ${context.delivered?'La livraison de la version consultée est déclarée.':'Aucune livraison n’est déduite de son cadrage.'}\n\nPour avancer, nous pouvons préciser le besoin que vous évoquez, comparer deux possibilités ou préparer une question pour le cadrage.\n\n**Quel résultat attendez-vous en priorité ?**`});
  p.projectChatBusy=false;p.projectChatRequest=null;
  if(project()===p){refRenderProjectChat();if(currentScreen()==='SCREEN-011'){$('#project-chat-messages').scrollTop=$('#project-chat-messages').scrollHeight;if(!p.archived)$('#project-chat-input').focus({preventScroll:true});}}
}

function refQuestions(v) {
  if (!v.questions) {
    const seeded = !v.uxFresh;
    v.questions = [
      {id:'public', title:'Qui utilisera cette première version ?', short:'Utilisateurs', context:'Définir les personnes concernées nous aide à choisir les besoins prioritaires.', recommendation:'Commencer avec les membres de l’atelier. La personne qui organise les disponibilités reste un utilisateur identifié.', rationale:'Ce premier périmètre répond au problème actuel de réservation sans multiplier les usages.', decision:seeded?{action:'answer',text:'Les membres de l’atelier et la personne qui organise les disponibilités.',source:'Réponse précédente'}:null},
      {id:'perimetre', title:'Quel problème résoudre en premier ?', short:'Périmètre prioritaire', context:'Les réservations passent aujourd’hui par des messages et un tableau au mur.', recommendation:'Retenir pour cette version la consultation des créneaux, la réservation d’un établi et la consultation de ses réservations.', rationale:'Un parcours complet permet de remplacer le fonctionnement actuel sans ajouter le paiement des adhésions.', decision:seeded?{action:'answer',text:'Consulter les disponibilités, réserver un établi et retrouver ses réservations.',source:'Réponse précédente'}:null},
      {id:'annulation', proposalId:1, title:'Faut-il pouvoir annuler une réservation ?', short:'Règle d’annulation', context:'Le créneau peut déjà avoir commencé. Il faut préciser jusqu’à quand une annulation est autorisée si cette fonctionnalité est retenue.', recommendation:'Inclure l’annulation dans cette version, uniquement avant le début du créneau. Une fois le créneau commencé, la réservation ne peut plus être annulée.', rationale:'La règle est compréhensible pour le membre et protège l’organisation de l’atelier.', decision:null}
    ];
    if (v.analysisDone === undefined) v.analysisDone = true;
    v.questions.forEach(q => {q.thread=[{author:'assistant',text:`## ${q.title}\n\n${q.context}\n\n**Ma recommandation**\n\n${q.recommendation}\n\nPourquoi ce choix ? ${q.rationale}\n\nVous pouvez me demander une alternative avant de décider.`}];});
  }
  return v.questions;
}
function refCurrentQuestion() {const items=refQuestions(version());return items.find(q=>q.id===refQuestionId)||items[0];}
function refDisposition(action) {return {answer:'Réponse enregistrée',retain:'Retenue pour cette version',defer:'Reportée à plus tard',refuse:'Refusée pour cette version',clarify:'À clarifier'}[action]||'À arbitrer';}
function refScrollCurrent(){
  if(!project())return;
  const screen=document.getElementById(currentScreen());if(!screen)return;
  $$('nav',screen).forEach(nav=>{const item=$('[aria-current="true"],[aria-current="step"]',nav);if(item&&nav.scrollWidth>nav.clientWidth){nav.scrollLeft+=item.getBoundingClientRect().left-nav.getBoundingClientRect().left-(nav.clientWidth-item.clientWidth)/2;}});
}
function refProposalSignature(p){return JSON.stringify([p.status,p.included,p.blocking,p.text]);}
function refSyncCancellation(){
  const v=version(),q=refQuestions(v).find(q=>q.id==='annulation'),p=v.proposals.find(p=>p.id===1);if(!p)return;
  const signature=refProposalSignature(p);
  if(q.signature!==undefined&&q.signature!==signature){
    q.decision=p.included?{action:'retain',text:p.text,source:'Arbitrage du cadrage'}:p.status==='deferred'?{action:'defer',text:p.text,source:'Arbitrage du cadrage'}:p.status==='refused'?{action:'refuse',text:p.text,source:'Arbitrage du cadrage'}:null;
    if(v.summaryApproved){invalidateSummary();v.summaryReady=true;}
  }
  q.signature=signature;
}
function refDiscussionSubject(){
  const v=version();if(!refDiscussionId.startsWith('proposal:'))return refQuestions(v).find(q=>q.id===refDiscussionId)||refCurrentQuestion();
  const id=Number(refDiscussionId.split(':')[1]),p=v.proposals.find(p=>p.id===id);v.proposalDiscussions||={};
  if(!v.proposalDiscussions[id])v.proposalDiscussions[id]={id:refDiscussionId,title:p.title,context:p.text,recommendation:'Conserver cette proposition hors du périmètre actuel tant que son inclusion et ses critères n’ont pas été examinés.',thread:[{author:'assistant',text:`## ${p.title}\n\n${p.text}\n\n**Ma recommandation**\n\nGardons ce besoin dans les éléments reportés si la version doit se concentrer sur la réservation. Nous pouvons examiner ensemble ce que son inclusion changerait.`}]};
  return v.proposalDiscussions[id];
}

// Sous-ensemble Markdown local, sans HTML brut, scripts ni dépendance distante.
function refMarkdown(text) {
  const inline=s=>esc(s).replace(/`([^`]+)`/g,'<code>$1</code>').replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>').replace(/\*([^*\n]+)\*/g,'<em>$1</em>');
  const lines=String(text).replace(/\r/g,'').split('\n');let output='',list='',code=false,buffer=[];
  const closeList=()=>{if(list){output+=`</${list}>`;list='';}};
  for(const line of lines){
    if(/^```/.test(line)){closeList();if(code){output+=`<pre><code>${esc(buffer.join('\n'))}</code></pre>`;buffer=[];}code=!code;continue;}
    if(code){buffer.push(line);continue;}
    if(!line.trim()){closeList();continue;}
    const heading=line.match(/^(#{1,4})\s+(.+)$/),item=line.match(/^\s*(?:([-*])|\d+\.)\s+(.+)$/);
    if(heading){closeList();const level=Math.min(heading[1].length+1,5);output+=`<h${level}>${inline(heading[2])}</h${level}>`;}
    else if(item){const type=item[1]?'ul':'ol';if(type!==list){closeList();list=type;output+=`<${list}>`;}output+=`<li>${inline(item[2])}</li>`;}
    else {closeList();output+=/^>\s?/.test(line)?`<blockquote>${inline(line.replace(/^>\s?/,''))}</blockquote>`:`<p>${inline(line)}</p>`;}
  }
  closeList();if(code)output+=`<pre><code>${esc(buffer.join('\n'))}</code></pre>`;return output;
}

function refRenderQuestion() {
  const v=version(),items=refQuestions(v),q=refCurrentQuestion(),answered=items.filter(q=>q.decision).length,locked=refLocked();
  $('#analysis-panel').hidden=!!v.analysisDone;$('#question-workspace').hidden=!v.analysisDone;
  $('#analysis-description').textContent=project().description;$('#analysis-error').hidden=!v.analysisError;
  $('[data-ref="analyse"]').disabled=locked||!!v.analysisBusy;$('#analysis-progress').hidden=!v.analysisBusy;
  $('#analysis-result').innerHTML=`<span class="check">✓</span> Analyse de départ réalisée <span class="quiet">· ${items.length-answered} question${items.length-answered===1?'':'s'} à préciser</span>`;
  $('#question-progress').textContent=`${answered} réponses enregistrées sur ${items.length}`;
  $('#question-list').innerHTML=items.map((item,i)=>`<button data-ref="select-question" data-question="${item.id}" aria-current="${item.id===q.id?'true':'false'}"><span class="question-number">${item.decision?'✓':i+1}</span><span>${esc(item.short)}<small>${item.preview?'Réponse à confirmer':item.decision?refDisposition(item.decision.action):'À examiner'}</small></span></button>`).join('');
  const isCancellation=q.id==='annulation';
  const decision=q.decision&&!q.editing?`<div class="saved-answer"><div class="section-heading"><h3>Votre décision</h3>${badge(refDisposition(q.decision.action),q.decision.action==='defer'?'grey':q.decision.action==='clarify'?'amber':'green')}</div><p>${esc(q.decision.text)}</p><p class="small quiet">${esc(q.decision.source)} · intégrée à la synthèse à relire.</p><button data-ref="edit-answer" ${locked?'disabled':''}>Modifier ma réponse</button></div>`:'';
  const answerForm=!q.decision||q.editing?`<div class="answer-choices"><button class="primary" data-ref="recommend" ${locked?'disabled':''}>Appliquer cette recommandation</button><button data-ref="discuss" data-question="${q.id}">Discuter avec l’IA</button></div><div class="custom-answer"><label for="question-answer">Ou donnez votre réponse</label><textarea id="question-answer" rows="3" ${locked?'disabled':''} placeholder="Ex. : je préfère reporter cette fonctionnalité à plus tard…">${esc(q.draft||'')}</textarea><div class="custom-answer-footer"><span class="help">Vous pouvez préciser, refuser ou reporter.</span><button data-ref="preview-answer" ${locked?'disabled':''}>Relire ma décision</button></div><p id="answer-error" class="field-error" hidden>Écrivez votre réponse avant de continuer.</p></div>`:`<button class="subtle-discussion" data-ref="discuss" data-question="${q.id}">Ouvrir la discussion liée à cette question</button>`;
  const preview=q.preview?`<div class="answer-preview" role="status"><h3>Ce qui sera ajouté à la synthèse</h3><p>${esc(q.preview.text)}</p>${isCancellation?`<label for="answer-disposition">Décision proposée d’après votre réponse</label><select id="answer-disposition">${['retain','defer','refuse','clarify'].map(a=>`<option value="${a}" ${q.preview.action===a?'selected':''}>${refDisposition(a)}</option>`).join('')}</select>`:''}<p class="help">Vérifiez l’interprétation. Votre texte restera associé à cette décision.</p><div class="actions"><button class="primary" data-ref="confirm-answer" ${locked?'disabled':''}>Confirmer cette décision</button><button data-ref="cancel-answer">Reprendre mon texte</button></div></div>`:'';
  $('#question-card').innerHTML=`<div class="question-card-meta"><span>Question ${items.indexOf(q)+1} sur ${items.length}</span>${badge('Cadrage fonctionnel')}</div><h2>${esc(q.title)}</h2><p class="question-context">${esc(q.context)}</p><div class="recommendation"><div class="recommendation-label"><span class="assistant-mark" aria-hidden="true">a</span><h3>Recommandation de l’IA</h3></div><div class="markdown">${refMarkdown(q.recommendation)}</div><p class="recommendation-why">${esc(q.rationale)}</p>${isCancellation?`<p class="recommendation-scope">Cette recommandation propose explicitement l’inclusion dans ${esc(v.id)}.</p>`:''}</div>${decision}${answerForm}${preview}<div class="question-navigation"><button data-ref="previous-question" ${items.indexOf(q)===0?'disabled':''}>Question précédente</button><button data-ref="next-question" ${items.indexOf(q)===items.length-1?'disabled':''}>Question suivante</button></div>`;
  $('[data-action="prepare-summary"]').disabled=locked||!v.analysisDone;
}

function refRenderSummary() {
  const v=version(),qs=refQuestions(v),doc=$('#SCREEN-006 .document');
  const afterHeading=(text)=>$$('h2',doc).find(h=>h.textContent===text)?.nextElementSibling;
  const objective=afterHeading('Objectif de la version');if(objective)objective.textContent=project().description;
  const audience=afterHeading('À qui s’adresse le projet ?');if(audience)audience.textContent=qs[0].decision?.text||'Les utilisateurs restent à préciser dans les questions de cadrage.';
  const included=afterHeading('Ce que nous retenons');if(included)included.innerHTML=v.features.map(f=>`<li>${esc(f.title)}</li>`).join('');
  const deferred=afterHeading('Ce que nous mettons de côté');if(deferred)deferred.textContent=v.proposals.filter(p=>p.status==='deferred'||p.status==='refused').map(p=>`${p.title} : ${p.status==='deferred'?'reportée':'refusée'}.`).join(' ')||'Aucun élément reporté ou refusé dans cette version.';
  const open=afterHeading('Points à préciser');if(open)open.textContent=blockers().length?'Une règle indispensable reste à clarifier pour une fonctionnalité retenue. La validation finale est bloquée.':qs.some(q=>!q.decision||q.decision.action==='clarify')?'Des questions restent à examiner. Aucune réponse ni proposition en attente n’est considérée comme approuvée.':'Les réponses de ce tour sont enregistrées. La synthèse reste à relire et à valider explicitement.';
  let section=$('#summary-decisions');if(!section){section=document.createElement('div');section.id='summary-decisions';$('#summary-edit').before(section);}
  section.innerHTML=`<h2>Décisions intégrées depuis vos réponses</h2>${qs.filter(q=>q.decision).map(q=>`<div class="summary-decision"><h3>${esc(q.short)} ${badge(refDisposition(q.decision.action))}</h3><p>${esc(q.decision.text)}</p></div>`).join('')||'<p>Aucune réponse enregistrée pour ce tour.</p>'}`;
}

function refRenderDiscussion() {
  const v=version(),q=refDiscussionSubject();
  $('#discussion-title').textContent='Discuter la recommandation';$('#discussion-question').textContent=q.title;
  $('[data-ref="return-question"]').textContent=refDiscussionId.startsWith('proposal:')?'Revenir à cette proposition pour décider':'Revenir à la question pour décider';
  $('#messages').innerHTML=q.thread.map(m=>`<article class="message ${m.author==='user'?'user':''}"><strong>${m.author==='user'?'Vous':'Assistant de cadrage'}</strong><div class="markdown">${refMarkdown(m.text)}</div></article>`).join('');
  $('#message').value=q.messageDraft||'';$('#ai-error').hidden=!v.aiError;$('#ai-loading').hidden=!busy;
}

renderInterview = function(){refBase.renderInterview();refRenderQuestion();refRenderSummary();refRenderDiscussion();};
renderProposals = function(){
  refBase.renderProposals();
  $$('#proposals-list .proposal').forEach(article=>{
    const discuss=$('[data-choice="discuss"]',article);const proposal=discuss?version().proposals.find(p=>String(p.id)===discuss.dataset.proposal):null;
    if(!proposal)return;
    const recommendation=document.createElement('div');recommendation.className='proposal-recommendation';
    recommendation.innerHTML=`<h3>Recommandation de l’IA</h3><p>${proposal.id===1?'Préciser une limite avant de retenir l’annulation. Vous pouvez aussi reporter cette fonctionnalité.':proposal.status==='deferred'?'Conserver cet élément hors du périmètre actuel. Son inclusion dans une autre version restera à décider.':'Examiner le besoin et ses critères avant toute inclusion dans cette version.'}</p>`;
    $('.actions',article).before(recommendation);
    discuss.removeAttribute('data-proposal');discuss.removeAttribute('data-choice');discuss.dataset.ref='discuss';discuss.dataset.question=proposal.id===1?'annulation':`proposal:${proposal.id}`;discuss.textContent='Discuter avec l’IA';
  });
};
showScreen = function(){refBase.showScreen();const id=currentScreen();$$('.phase-link').forEach(a=>{if(['SCREEN-005','SCREEN-006','SCREEN-007','SCREEN-008','SCREEN-009'].includes(id))a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');});if(id==='SCREEN-011'){$('#version-banner').hidden=true;refRenderProjectChat();}refScrollCurrent();};
// Le listener existant conserve sa référence d’origine ; la synchronisation de la phase est aussi liée au hash.
window.addEventListener('hashchange',()=>{if(project())showScreen();});
render = function(){
  const drawerOpen=$('#discussion').open,active=document.activeElement?.id;
  if(project())refSyncCancellation();
  refBase.render();if(!project())return;
  refRenderProjectChat();
  $$('[data-ref="recommend"],[data-ref="confirm-answer"],[data-ref="preview-answer"],[data-ref="edit-answer"]').forEach(b=>b.disabled=refLocked());
  if(drawerOpen&&active==='message')$('#message').focus({preventScroll:true});
  if(!version().analysisDone){$('#resume-heading').textContent='Une idée à analyser.';$('#resume-copy').textContent='L’analyse prépare les questions qui vous aideront à construire le périmètre de cette version.';$('#resume-link').textContent=project().archived?'Consulter le cadrage':'Commencer l’analyse';}
};
makeVersion = function(id){const v=refBase.makeVersion(id);v.uxFresh=true;v.analysisDone=false;return v;};
snapshot = function(label){refBase.snapshot(label);version().snapshots.at(-1).content.decisions=clone(refQuestions(version()).filter(q=>q.decision).map(q=>({question:q.title,...q.decision})));};
reset = function(scenario='interview'){
  if($('#discussion').open)$('#discussion').close();refAnalysisBusy=false;refQuestionId='annulation';
  refBase.reset(scenario);
  projects.forEach(p=>p.versions.forEach(v=>{v.uxFresh=['initial-analysis','analysis-error'].includes(scenario);v.analysisDone=!['initial-analysis','analysis-error'].includes(scenario);delete v.questions;refQuestions(v);v.history.forEach(e=>{if(e.title==='Entretien commencé')e.title='Cadrage commencé';});if(['summary','catalogue','ready','approved','delivered'].includes(scenario)){v.questions[2].decision={action:'defer',text:'Reporter l’annulation à une autre version.',source:'Réponse précédente'};v.proposals.find(p=>p.id===1).status='deferred';}if(scenario==='analysis-error')v.analysisError=true;}));
  if(['initial-analysis','analysis-error'].includes(scenario))refQuestionId='public';
  render();
  if(scenario==='ai-error'){refQuestions(version())[2].thread.push({author:'user',text:'Pourquoi recommandez-vous une annulation avant le début du créneau ?'});refOpenDiscussion('annulation');}
  if(scenario==='project-chat-error'){const p=project();refProjectChat(p).push({author:'user',text:'Quel besoin devrions-nous clarifier en premier ?',contextVersion:p.selectedVersion});p.projectChatRequest=refProjectChatContext(p);p.projectChatError=true;refRenderProjectChat();navigate('SCREEN-011');}
};

function refOpenDiscussion(id){
  refDiscussionId=id;refRenderDiscussion();if(!$('#discussion').open)$('#discussion').showModal();
  if(!refLocked()&&!version().aiError)$('#message').focus();
}
function refRecordDecision(q,decision){
  if(!writable())return;
  const v=version();q.decision=decision;q.preview=null;q.editing=false;
  if(q.proposalId){const p=v.proposals.find(p=>p.id===q.proposalId);p.status=decision.action==='retain'?'accepted':decision.action==='defer'?'deferred':decision.action==='refuse'?'refused':'pending';p.included=decision.action==='retain';p.blocking=p.included&&!/avant|interdit.*apr[eè]s|pas.*apr[eè]s/i.test(decision.text);p.text=decision.text;
    v.features=v.features.filter(f=>f.id!=='FONC-003');if(p.included){const f=cancellationFeature(p);f.behavior=decision.text;f.criteria=[decision.text];v.features.push(f);}q.signature=refProposalSignature(p);
  }
  invalidateSummary();v.summaryReady=true;
  addEvent('Réponse de cadrage enregistrée',`${q.title}\n${refDisposition(decision.action)}\n${decision.text}\nOrigine : ${decision.source}. La synthèse reste à valider.`);
  render();toast('Réponse intégrée à la synthèse à relire.');
}
async function refAnalyse(){
  if(!writable()||version().analysisBusy)return;const v=version(),token=generation;v.analysisBusy=true;v.analysisError=false;render();
  await new Promise(resolve=>setTimeout(resolve,900));if(token!==generation)return;
  v.analysisBusy=false;v.analysisDone=true;v.history.unshift({title:'Analyse de départ préparée',detail:'Objectif et contexte identifiés. Questions de cadrage proposées, sans validation de périmètre.',origin:'Assistant IA'});render();toast('Analyse terminée. Les questions de cadrage sont prêtes.');
}

// Les échanges sont propres à la question ouverte et ne changent jamais ses décisions.
respond = async function(){
  if(!writable()||busy)return;const v=version(),q=refDiscussionSubject(),token=generation;
  v.aiError=false;busy=true;render();
  await new Promise(resolve=>setTimeout(resolve,850));if(token!==generation)return;
  q.thread.push({author:'assistant',text:`### Deux possibilités à comparer\n\n- **Retenir un périmètre simple** : ${q.recommendation}\n- **Reporter ce point** : conserver l’idée sans l’inclure dans cette version.\n\n${q.id==='annulation'?'Par exemple, « je préfère reporter l’annulation » sera proposé comme un report à confirmer.':'Votre réponse libre peut préciser les utilisateurs ou modifier le périmètre proposé.'}\n\n**Pour décider**, revenez à la question et appliquez la recommandation ou enregistrez votre propre réponse.`});
  busy=false;render();$('#messages').scrollTop=$('#messages').scrollHeight;
};
// Remplacer seulement le formulaire d’échange : les autres formulaires restent ceux de la galerie.
const refMessageForm=$('#message-form'),refMessageClone=refMessageForm.cloneNode(true);refMessageForm.replaceWith(refMessageClone);
$('#message-form').addEventListener('submit',event=>{event.preventDefault();if(!writable()||busy||version().aiError)return;const text=$('#message').value.trim();if(!text)return;const q=refDiscussionSubject();q.thread.push({author:'user',text});q.messageDraft='';$('#message').value='';respond();});
$('#message').addEventListener('keydown',event=>{if(event.key==='Enter'&&!event.shiftKey&&!event.isComposing){event.preventDefault();if(!$('#send-message').disabled)$('#message-form').requestSubmit();}});
$('#message').addEventListener('input',event=>{const q=refDiscussionSubject();q.messageDraft=event.target.value;event.target.style.height='auto';event.target.style.height=Math.min(event.target.scrollHeight,180)+'px';});

document.addEventListener('input',event=>{if(event.target.id==='question-answer')refCurrentQuestion().draft=event.target.value;});
document.addEventListener('click',event=>{
  const b=event.target.closest('[data-ref]');if(!b)return;const command=b.dataset.ref;
  if(command==='analyse'){refAnalyse();return;}
  if(command==='close-discussion'||command==='return-question'){$('#discussion').close();if(command==='return-question'){if(refDiscussionId.startsWith('proposal:')){navigate('SCREEN-007');}else{refQuestionId=refDiscussionId;render();navigate('SCREEN-005');}}return;}
  if(command==='discuss'){refOpenDiscussion(b.dataset.question||refCurrentQuestion().id);return;}
  const qs=refQuestions(version()),q=refCurrentQuestion();
  if(command==='select-question'){refQuestionId=b.dataset.question;render();}
  if(command==='previous-question'||command==='next-question'){const delta=command==='next-question'?1:-1;refQuestionId=qs[Math.max(0,Math.min(qs.length-1,qs.indexOf(q)+delta))].id;render();}
  if(command==='recommend')refRecordDecision(q,{action:q.id==='annulation'?'retain':'answer',text:q.recommendation,source:'Recommandation appliquée explicitement'});
  if(command==='edit-answer'){if(!writable())return;q.editing=true;q.draft=q.decision.text;render();$('#question-answer').focus();}
  if(command==='preview-answer'){
    if(!writable())return;const text=$('#question-answer').value.trim();if(!text){$('#answer-error').hidden=false;$('#question-answer').focus();return;}
    const action=q.id!=='annulation'?'answer':/report|plus tard|version suivante/i.test(text)?'defer':/refus|exclu|abandon|annul(?:e|er|ons) (?:cette|la) fonctionnalit|pas (?:d.annulation|de fonctionnalit)/i.test(text)?'refuse':/avant|uniquement|autoriser|retenir|inclur/i.test(text)?'retain':'clarify';
    q.preview={text,action};q.draft=text;render();$('.answer-preview').scrollIntoView({block:'nearest'});
  }
  if(command==='confirm-answer'){const action=$('#answer-disposition')?.value||q.preview.action;refRecordDecision(q,{action,text:q.preview.text,source:'Réponse libre confirmée'});}
  if(command==='cancel-answer'){q.preview=null;render();$('#question-answer').focus();}
});

actions.suspend=()=>{if(!writable())return;openDialog('Suspendre ce cadrage ?','<p>Les réponses enregistrées, les discussions et les questions ouvertes sont conservées. Une suspension ne valide aucun résultat.</p>','','Suspendre et revenir au projet',()=>{version().suspended=true;version().active=false;addEvent('Cadrage suspendu','Questions et réponses conservées. Aucune approbation implicite.');render();navigate('SCREEN-003');});};
actions['prepare-summary']=()=>{if(!writable())return;if(!version().analysisDone){toast('Analysez l’idée avant de préparer la synthèse.');return;}version().summaryReady=true;addEvent('Synthèse préparée','Synthèse proposée à partir des réponses confirmées. Une validation explicite reste attendue.','Assistant IA');render();navigate('SCREEN-006');};
$('#theme-toggle').addEventListener('click',()=>{const dark=document.documentElement.dataset.theme!=='dark';document.documentElement.dataset.theme=dark?'dark':'light';$('#theme-toggle').setAttribute('aria-label',dark?'Passer au thème clair':'Passer au thème sombre');$('#theme-toggle span').textContent=dark?'Thème clair':'Thème sombre';$('#theme-toggle').firstChild.textContent=dark?'☀ ':'☾ ';});
$('.context-right').append($('#theme-toggle'));
$('#project-chat-form').addEventListener('submit',event=>{event.preventDefault();const p=project();if(!p||p.archived||p.projectChatBusy||p.projectChatError)return;const text=$('#project-chat-input').value.trim();if(!text)return;p.projectChatRequest=refProjectChatContext(p);refProjectChat(p).push({author:'user',text,contextVersion:p.selectedVersion});p.projectChatDraft='';$('#project-chat-input').value='';refProjectChatRespond();});
$('#project-chat-input').addEventListener('input',event=>{project().projectChatDraft=event.target.value;event.target.style.height='auto';event.target.style.height=Math.min(event.target.scrollHeight,180)+'px';});
$('#project-chat-input').addEventListener('keydown',event=>{if(event.key==='Enter'&&!event.shiftKey&&!event.isComposing){event.preventDefault();if(!$('#project-chat-send').disabled)$('#project-chat-form').requestSubmit();}});
$('#project-chat-retry').addEventListener('click',refProjectChatRespond);
$$('.steps a[href="#SCREEN-005"]').forEach(a=>a.textContent='Questions');
$$('.steps').filter(nav=>!$('a[href="#SCREEN-007"]',nav)).forEach(nav=>nav.insertAdjacentHTML('beforeend','<a href="#SCREEN-007">Décisions et reports</a>'));
$('#version-needs').nextElementSibling.textContent='Les éléments reportés restent à sélectionner dans le cadrage de cette version. Aucun n’est ajouté automatiquement.';
$('#resume-link').textContent='Reprendre le cadrage';
const refInitialScreen=currentScreen();reset('interview');navigate(refInitialScreen);
window.addEventListener('load',()=>window.scrollTo(0,0));
