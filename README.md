<<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ScholarshipSys</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

<style>
body {
  background: url("images/books-bg.jpeg") no-repeat center center fixed;
  background-size: cover;
  font-family: 'Segoe UI', sans-serif;
  color: white;
  min-height: 100vh;
}
.navbar { background: rgba(0,0,0,0.7); }

.hero {
  text-align: center;
  margin-top: 100px;
  background: rgba(0,0,0,0.6);
  padding: 30px;
  border-radius: 15px;
  width: 70%;
  margin:auto;
}

.footer { text-align: center; padding: 30px; }

.btn-big {
  width: 250px;
  height: 70px;
  margin: 15px;
}

.chatbot-icon {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background: #0dcaf0;
  border-radius: 50%;
  width: 65px;
  height: 65px;
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:30px;
  cursor:pointer;
}

.chatbox {
  position: fixed;
  bottom: 100px;
  right: 20px;
  width: 300px;
  background: black;
  padding: 10px;
  border-radius: 10px;
  display:none;
}

.section-box {
  background: rgba(255,255,255,0.1);
  padding: 15px;
  border-radius: 10px;
}
</style>
</head>

<body>

<!-- NAVBAR -->
<nav class="navbar navbar-expand-lg">
<div class="container-fluid">

<span class="navbar-brand text-warning">ScholarshipSys</span>

<div class="mx-auto">
<ul class="navbar-nav flex-row gap-3">
  <li><a class="nav-link text-white" href="doc.html">Home</a></li>
  <li><a class="nav-link text-white" href="scholarships.html">Scholarship</a></li>
  <li><a class="nav-link text-white" href="#">Career Guidance</a></li>
  <li><a class="nav-link text-white" href="#">Loan Guidance</a></li>
  <li><a class="nav-link text-white" href="#">About</a></li>
  <li><a class="nav-link text-white" href="#">Contact</a></li>
</ul>
</div>

<select onchange="changeLang(this.value)" class="form-select w-auto bg-dark text-white">
<option value="en">English</option>
<option value="ta">Tamil</option>
</select>

</div>
</nav>

<!-- HERO -->
<div class="hero">
<h1 id="quote">Education is the passport to the future</h1>
</div>

<!-- BUTTONS -->
<div class="footer">
<button class="btn btn-success btn-big" data-bs-toggle="modal" data-bs-target="#modal">Add Credentials</button>
<button class="btn btn-primary btn-big">Update Credentials</button>
</div>

<!-- CHATBOT -->
<div class="chatbot-icon" onclick="toggleChat()">💬</div>

<div class="chatbox" id="chatbox">
<div id="chatContent" style="height:150px;overflow:auto"></div>
<input type="text" id="chatInput" class="form-control mt-2">
<button class="btn btn-info w-100 mt-2" onclick="sendMsg()">Send</button>
</div>

<!-- MAIN MODAL -->
<div class="modal fade" id="modal">
<div class="modal-dialog modal-lg">
<div class="modal-content bg-dark text-white">

<div class="modal-header">
<h5>User Profile</h5>
<button class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
</div>

<div class="modal-body">

<div class="text-center">
<img id="preview" src="https://via.placeholder.com/100" class="rounded-circle">
<input type="file" id="photo" class="form-control w-50 mx-auto mt-2">
<h5 id="usernameDisplay">No Name</h5>
<p id="emailDisplay">No Email</p>
</div>

<div class="progress my-3">
<div id="progressBar" class="progress-bar bg-success" style="width:0%">0%</div>
</div>

<div class="d-grid gap-2">
<button class="btn btn-outline-info" data-bs-toggle="modal" data-bs-target="#aboutModal">About</button>
<button class="btn btn-outline-info" data-bs-toggle="modal" data-bs-target="#educationModal">Education</button>
<button class="btn btn-outline-info" onclick="show('documents')">Documents</button>
<button class="btn btn-outline-info" data-bs-toggle="modal" data-bs-target="#achievementsModal">Achievements</button>
</div>

<button class="btn btn-warning mt-3" onclick="runAI()">🤖 AI Guidance</button>

<div id="content" class="section-box mt-3">Select section / AI guidance</div>

<hr>

<form id="form">
<input id="username" placeholder="Username" class="form-control mb-2">
<input id="email" placeholder="Email" class="form-control mb-2">
<input id="password" type="password" placeholder="Password" class="form-control mb-2">
<input id="cgpa" placeholder="CGPA" class="form-control mb-2">
<button class="btn btn-success">Save</button>
</form>

</div>
</div>
</div>
</div>

<!-- ABOUT MODAL -->
<div class="modal fade" id="aboutModal">
<div class="modal-dialog modal-fullscreen">
<div class="modal-content">

<div class="modal-header bg-dark text-white">
<h5>Student Details</h5>
<button class="btn btn-light" data-bs-dismiss="modal">⬅ Back</button>
</div>

<div class="modal-body" style="background:#f5f5f5;color:black;overflow-y:auto">

<div id="guideBox" class="alert alert-info" style="display:none;"></div>

<form id="aboutForm">

<input class="form-control mb-2" placeholder="First Name" onfocus="guide('Enter your first name')">
<input class="form-control mb-2" placeholder="Last Name" onfocus="guide('Enter your last name')">
<input type="date" class="form-control mb-2" onfocus="guide('Select your date of birth')">

<input class="form-control mb-2" placeholder="Father Name" onfocus="guide('Enter father name')">
<input class="form-control mb-2" placeholder="Mother Name" onfocus="guide('Enter mother name')">
<input class="form-control mb-2" placeholder="Siblings" onfocus="guide('Enter siblings')">

<input class="form-control mb-2" placeholder="Father Occupation" onfocus="guide('Enter father occupation')">
<input class="form-control mb-2" placeholder="Mother Occupation" onfocus="guide('Enter mother occupation')">

<input class="form-control mb-2" placeholder="Student Mobile" onfocus="guide('Enter your mobile number')">
<input class="form-control mb-2" placeholder="Father Mobile" onfocus="guide('Enter father mobile number')">
<input class="form-control mb-2" placeholder="Mother Mobile" onfocus="guide('Enter mother mobile number')">

<textarea class="form-control mb-2" placeholder="Address" onfocus="guide('Enter your home address')"></textarea>

<input class="form-control mb-2" placeholder="PIN Code" onfocus="guide('Enter your pin code')">
<input class="form-control mb-2" placeholder="City" onfocus="guide('Enter your city')">
<input class="form-control mb-2" placeholder="Village" onfocus="guide('Enter your village')">
<input class="form-control mb-2" placeholder="District" onfocus="guide('Enter your district')">

<input class="form-control mb-2" placeholder="Income" onfocus="guide('Enter your annual income')">

<button class="btn btn-primary w-100">Save</button>

</form>

</div>
</div>
</div>
</div>

<!-- EDUCATION MODAL -->
<div class="modal fade" id="educationModal">
<div class="modal-dialog modal-fullscreen">
<div class="modal-content">

<div class="modal-header bg-dark text-white">
<h5>Education Details</h5>
<button class="btn btn-light" data-bs-dismiss="modal">⬅ Back</button>
</div>

<div class="modal-body" style="background:#f5f5f5;color:black;overflow-y:auto">

<div id="eduGuide" class="alert alert-info" style="display:none;"></div>

<form>

<input class="form-control mb-2" placeholder="Age" onfocus="eduGuideSpeak('Enter your age')">
<input class="form-control mb-2" placeholder="School Name" onfocus="eduGuideSpeak('Enter your school name')">

<select class="form-control mb-2" id="studyLevel" onchange="handleEducation()" onfocus="eduGuideSpeak('Select study level')">
<option>Select Current Study</option>
<option>Class 1-10</option>
<option>Class 12</option>
<option>Class 12 Passed</option>
<option>Diploma / Polytechnic</option>
<option>ITI</option>
<option>Vocational Course</option>
<option>Coaching Class</option>
<option>Undergraduate</option>
<option>Postgraduate</option>
</select>

<div id="eduDynamic"></div>

<button class="btn btn-primary w-100 mt-3">Save Education</button>

</form>

</div>
</div>
</div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

<script>

// IMAGE
photo.onchange = e=>{
let r=new FileReader();
r.onload=()=>preview.src=r.result;
r.readAsDataURL(e.target.files[0]);
};

// PROFILE %
function updateProgress(){
let inputs=document.querySelectorAll("input,textarea");
let filled=0;
inputs.forEach(i=>{if(i.value)filled++;});
let percent=Math.round((filled/inputs.length)*100);
progressBar.style.width=percent+"%";
progressBar.innerText=percent+"%";
}
document.querySelectorAll("input,textarea").forEach(el=>{
el.addEventListener("input",updateProgress);
});

// GUIDE
function guide(msg){
guideBox.style.display="block";
guideBox.innerText="👉 "+msg;
speechSynthesis.speak(new SpeechSynthesisUtterance(msg));
setTimeout(()=>guideBox.style.display="none",2000);
}

// EDUCATION GUIDE
function eduGuideSpeak(msg){
eduGuide.style.display="block";
eduGuide.innerText="👉 "+msg;
speechSynthesis.speak(new SpeechSynthesisUtterance(msg));
setTimeout(()=>eduGuide.style.display="none",2000);
}

// EDUCATION LOGIC
function handleEducation(){
let level=studyLevel.value;
let html="";

if(level!=="Class 1-10"){
html+=`<h5>10th</h5>
<input class="form-control mb-2" placeholder="10th School">
<input class="form-control mb-2" placeholder="10th Marks">
<input class="form-control mb-2" placeholder="10th Year">`;
}

if(level==="Class 12"||level==="Class 12 Passed"||level==="Undergraduate"||level==="Postgraduate"){
html+=`<h5>12th</h5>
<input class="form-control mb-2" placeholder="12th School">
<input class="form-control mb-2" placeholder="12th Marks">
<input class="form-control mb-2" placeholder="12th Year">`;
}

if(level==="Undergraduate"||level==="Postgraduate"){
html+=`<h5>UG</h5>
<input class="form-control mb-2" placeholder="College">
<input class="form-control mb-2" placeholder="CGPA">
<input class="form-control mb-2" placeholder="Year">`;
}

if(level==="Postgraduate"){
html+=`<h5>PG</h5>
<input class="form-control mb-2" placeholder="PG College">
<input class="form-control mb-2" placeholder="PG CGPA">
<input class="form-control mb-2" placeholder="Year">`;
}

eduDynamic.innerHTML=html;
}

// CHAT
function toggleChat(){chatbox.style.display=chatbox.style.display==="none"?"block":"none";}
function sendMsg(){
chatContent.innerHTML+="<p>🧑 "+chatInput.value+"</p>";
chatContent.innerHTML+="<p>🤖 Try scholarship portal</p>";
chatInput.value="";
}

// AI
function runAI(){
content.innerHTML=cgpa.value>=8?"🎯 Eligible":"📘 Improve profile";
}

// LANG
function changeLang(l){
quote.innerText=l==="ta"?"கல்வியே எதிர்காலத்தின் சாவி":"Education is the passport to the future";
}

</script>
<script>

// ================= DOCUMENT FEATURE (FINAL COMBINED) =================

let documents = {};

// Store old show
const oldShow = typeof show === "function" ? show : null;

// Override documents section
function show(s){

if(s==="documents"){

// 🔊 Voice Guidance when opening
docSpeak("Welcome to document section. Please upload required documents.");

content.innerHTML = `

<button class="btn btn-secondary mb-2" onclick="goBack()">⬅ Back</button>

<h4>📂 My Document Wallet</h4>

<div>
${docItem("aadhaar","Aadhaar Card")}
${docItem("10th","10th Marksheet")}
${docItem("12th","12th Marksheet")}
${docItem("college","College ID")}
${docItem("income","Income Certificate")}
${docItem("community","Community Certificate")}
${docItem("residence","Residence Certificate")}
${docItem("bonafide","Bonafide Certificate")}
</div>

<hr>

<h5>📊 Document Completion</h5>
<div class="progress">
<div id="docProgress" class="progress-bar bg-success" style="width:0%">0%</div>
</div>

<div id="aiSuggestion" class="mt-3 alert alert-warning">
🤖 Upload documents to get suggestions
</div>

`;

updateDocProgress();
runDocAI();
return;
}

// other sections
if(oldShow) oldShow(s);
}

// ================= DOCUMENT UI =================

function docItem(id,name){
return `
<div class="d-flex justify-content-between align-items-center border p-2 mb-2 rounded bg-dark text-white">

<span>📄 ${name}</span>

<div>
<input type="file" onchange="uploadDoc('${id}',this)" hidden id="${id}">
<button class="btn btn-sm btn-info" onclick="triggerUpload('${id}','${name}')">Upload</button>

<span id="${id}_status" class="ms-2 text-danger">❌ Missing</span>

<button class="btn btn-sm btn-danger ms-2" onclick="removeDoc('${id}')">Delete</button>
</div>

</div>

<div id="${id}_preview" class="text-info small mb-2"></div>
`;
}

// ================= UPLOAD =================

function triggerUpload(id,name){
docSpeak("Upload your " + name);
document.getElementById(id).click();
}

function uploadDoc(id,input){
let file = input.files[0];
if(!file) return;

documents[id] = file.name;

document.getElementById(id+"_status").innerHTML = "✔ Uploaded";
document.getElementById(id+"_status").classList.remove("text-danger");
document.getElementById(id+"_status").classList.add("text-success");

document.getElementById(id+"_preview").innerHTML = "📁 "+file.name;

// 🔊 Voice
docSpeak("Document uploaded successfully");

updateDocProgress();
runDocAI();
}

// ================= DELETE =================

function removeDoc(id){
delete documents[id];

document.getElementById(id+"_status").innerHTML = "❌ Missing";
document.getElementById(id+"_status").classList.add("text-danger");

document.getElementById(id+"_preview").innerHTML = "";

// 🔊 Voice
docSpeak("Document removed");

updateDocProgress();
runDocAI();
}

// ================= PROGRESS =================

function updateDocProgress(){
let total = 8;
let uploaded = Object.keys(documents).length;
let percent = Math.round((uploaded/total)*100);

let bar = document.getElementById("docProgress");
if(bar){
bar.style.width = percent+"%";
bar.innerText = percent+"%";
}
}

// ================= AI SUGGESTION =================

function runDocAI(){
let msg="🤖 ";

if(!documents["income"]) msg+="Upload Income Certificate for Govt Scholarships<br>";
if(!documents["aadhaar"]) msg+="Aadhaar required for verification<br>";
if(documents["10th"] && documents["12th"]) msg+="🎯 Eligible for Merit Scholarships<br>";

if(Object.keys(documents).length===8){
msg="🎉 All documents uploaded! Ready to apply!";
}

let aiBox = document.getElementById("aiSuggestion");
if(aiBox) aiBox.innerHTML=msg;
}
// ================= VOICE GUIDANCE =================

function docSpeak(text){
let speech = new SpeechSynthesisUtterance(text);
speech.lang = "en-IN";
window.speechSynthesis.speak(speech);
}

// ===================================================

</script>
<div class="modal fade" id="achievementsModal" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-fullscreen">
    <div class="modal-content">
      <div class="modal-header bg-dark text-white">
        <h5 class="modal-title">🏆 My Achievements & Recognition</h5>
        <button type="button" class="btn btn-light" data-bs-dismiss="modal">⬅ Back to Profile</button>
      </div>

      <div class="modal-body" style="background:#f4f7f6; color:black; overflow-y:auto">
        
        <div class="container mb-4">
          <div class="row g-3">
            <div class="col-md-6">
              <div class="card shadow-sm border-0 p-3 h-100">
                <div class="d-flex justify-content-between align-items-center mb-2">
                  <h6 class="mb-0 fw-bold">🎯 Profile Strength Score</h6>
                  <span id="scoreText" class="badge bg-primary">0 Points</span>
                </div>
                <div class="progress" style="height: 20px; border-radius: 10px;">
                  <div id="achScoreBar" class="progress-bar progress-bar-striped progress-bar-animated bg-warning text-dark fw-bold" style="width:0%">0%</div>
                </div>
                <small class="text-muted mt-2">Add more achievements to hit 100%!</small>
              </div>
            </div>
            <div class="col-md-6">
              <div id="achAIBox" class="card shadow-sm border-0 p-3 h-100 bg-info text-white">
                <div class="d-flex align-items-center">
                  <span style="font-size: 2rem;" class="me-3">🤖</span>
                  <div>
                    <h6 class="fw-bold mb-1">AI Career Guidance</h6>
                    <p id="aiSuggestionText" class="small mb-0">Add your first achievement to unlock personalized scholarship suggestions.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="container">
          <div id="achList">
            </div>

          <div class="text-center mt-4 mb-5">
            <button class="btn btn-primary btn-lg px-5 shadow" onclick="addAchievement()">
              ➕ Add Achievement Entry
            </button>
          </div>
        </div>

      </div>
    </div>
  </div>
</div>

<script>
let achievementCounter = 0;

/**
 * Adds a new dynamic achievement form card
 */
function addAchievement() {
  achievementCounter++;
  const id = ach_row_${achievementCounter};
  
  const achHTML = `
    <div class="card shadow-sm mb-4 border-0 border-start border-primary border-4" id="card_${id}" style="transition: 0.3s;">
      <div class="card-body">
        <div class="d-flex justify-content-between align-items-center mb-3">
          <h5 class="text-primary mb-0">Recognition #${achievementCounter}</h5>
          <button class="btn btn-sm btn-outline-danger border-0" onclick="removeAch('${id}')">
            🗑 Delete
          </button>
        </div>
        
        <div class="row g-3">
          <div class="col-md-6">
            <label class="form-label small fw-bold">Achievement Title</label>
            <input type="text" class="form-control" placeholder="e.g. State Level Hackathon Winner" onfocus="achSpeak('Enter your achievement title')">
          </div>
          
          <div class="col-md-3">
            <label class="form-label small fw-bold">Date Received</label>
            <input type="date" class="form-control" onfocus="achSpeak('When did you receive this?')">
          </div>
          
          <div class="col-md-3">
            <label class="form-label small fw-bold">Category (Weightage)</label>
            <select class="form-select ach-type-select" onchange="updateSystem()" onfocus="achSpeak('Select the category')">
              <option value="0" selected disabled>Choose Type</option>
              <option value="30">Academic (+30)</option>
              <option value="25">Technical (+25)</option>
              <option value="20">Sports (+20)</option>
              <option value="15">Cultural (+15)</option>
            </select>
          </div>

          <div class="col-md-6">
            <label class="form-label small fw-bold">Issued By</label>
            <input type="text" class="form-control" placeholder="University / Organization Name" onfocus="achSpeak('Enter the issuing authority')">
          </div>

          <div class="col-md-6">
            <label class="form-label small fw-bold">Certificate Upload</label>
            <input type="file" class="form-control" onchange="achSpeak('Document attached successfully')">
          </div>

          <div class="col-md-12">
            <label class="form-label small fw-bold">Description / Impact</label>
            <textarea class="form-control" rows="2" placeholder="Briefly explain your role or the significance..." onfocus="achSpeak('Give a short description')"></textarea>
          </div>
        </div>
      </div>
    </div>
  `;
  
  document.getElementById('achList').insertAdjacentHTML('beforeend', achHTML);
  updateSystem();
  achSpeak("New entry added. Please fill in the details.");
}

/**
 * Removes an entry and updates the score
 */
function removeAch(id) {
  const element = document.getElementById(card_${id});
  element.style.opacity = '0';
  setTimeout(() => {
    element.remove();
    updateSystem();
    achSpeak("Entry deleted");
  }, 300);
}

/**
 * Main Controller: Updates Score and AI Suggestions
 */
function updateSystem() {
  let totalScore = 0;
  let categories = [];
  
  // 1. Calculate Score
  const selects = document.querySelectorAll('.ach-type-select');
  selects.forEach(select => {
    const val = parseInt(select.value) || 0;
    totalScore += val;
    if(val > 0) categories.push(select.options[select.selectedIndex].text);
  });

  // 2. Update Progress Bar (Cap at 100)
  const cappedPercent = Math.min(totalScore, 100);
  const bar = document.getElementById('achScoreBar');
  bar.style.width = cappedPercent + "%";
  bar.innerText = cappedPercent + "%";
  document.getElementById('scoreText').innerText = totalScore + " Points";

  // 3. AI Suggestion Logic
  const aiText = document.getElementById('aiSuggestionText');
  const aiCard = document.getElementById('achAIBox');
  
  if (totalScore === 0) {
    aiText.innerHTML = "Your profile needs more weight. Participate in <strong>Technical Symposiums</strong> or <strong>Academic Competitions</strong> to stand out.";
    aiCard.className = "card shadow-sm border-0 p-3 h-100 bg-secondary text-white";
  } else if (categories.some(c => c.includes("Technical"))) {
    aiText.innerHTML = "Excellent! Since you have <strong>Technical achievements</strong>, you are eligible for the <em>Innovation in STEM Scholarship</em>.";
    aiCard.className = "card shadow-sm border-0 p-3 h-100 bg-success text-white";
  } else if (totalScore >= 70) {
    aiText.innerHTML = "🎯 <strong>Elite Profile!</strong> You have a high chance of securing <em>International Merit Scholarships</em>. Keep it up!";
    aiCard.className = "card shadow-sm border-0 p-3 h-100 bg-warning text-dark";
  } else {
    aiText.innerHTML = "Good progress. Adding an <strong>Academic</strong> certificate will significantly boost your profile for Government scholarships.";
    aiCard.className = "card shadow-sm border-0 p-3 h-100 bg-info text-white";
  }
}

/**
 * Browser-based Text-to-Speech
 */
function achSpeak(text) {
  if ('speechSynthesis' in window) {
    window.speechSynthesis.cancel(); // Stop overlap
    const speech = new SpeechSynthesisUtterance(text);
    speech.rate = 1.0;
    speech.pitch = 1.0;
    window.speechSynthesis.speak(speech);
  }
}
</script>
