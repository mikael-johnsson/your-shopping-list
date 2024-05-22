

// Delete list confirmation modal
const deleteListButton = document.getElementById('delete-list-button')
function showDeleteListModal(){
    const deleteConfirmationModal = document.getElementById("delete-confirmation-modal")
    const modal = new bootstrap.Modal(deleteConfirmationModal);
    modal.show();
}


if(deleteListButton){ 
    deleteListButton.addEventListener("click", showDeleteListModal)
}

// Share list modal
const shareListButton = document.getElementById("share-list-button")
function shareListModal(){
    const emailModal = document.getElementById("share-list-modal")
    const modal = new bootstrap.Modal(emailModal);
    modal.show();
}


if(shareListButton){ 
    shareListButton.addEventListener("click", shareListModal)
}

// Share list function
function sendMail(shareList) {
    let listName = document.getElementById("list-name")
    let listItemElements = document.getElementsByClassName("list-items")
    let listItemValues = []
    for (let element of listItemElements){
        let value = element.textContent
        listItemValues.push(value)
    }
    
    emailjs.send("service_s8rbn75","template_zvdv8q9", {
        "from_name" : shareList.senderName.value,
        "to_email": shareList.emailInput.value,
        "list_name": listName.textContent,
        "list_items": listItemValues,
        "message": shareList.message.value
    })
    .then(
        function(response) {
            console.log("success", response);
        },
        function(error) {
            console.log("fail", error);
        }
    );
    
}
    
// Give new list a name modal
const newListModal = document.getElementById("new-list-modal")
function showNewListModal(){
    const modal = new bootstrap.Modal(newListModal);
    modal.show();
}

newListModalButton = document.getElementById("create-list-button")
if(newListModalButton) {
    newListModalButton.addEventListener("click", showNewListModal )
}


// Edit items section//
const editListButton = document.getElementById("edit-list-button")
const editButtons = document.getElementsByClassName("item-edit-button")
const deleteButtons = document.getElementsByClassName("delete-item-button")
const updateForms = document.getElementsByClassName("item-edit-form")

//Hide item buttons and update forms
for (let button of editButtons){
    button.style.display = "none"
}

for (let button of deleteButtons){
    button.style.display = "none"
}
for (let form of updateForms){
    form.style.display = "none"
}

//Display item buttons
function showItemButtons(){
    for (let button of editButtons){
        button.style.display = "block"
    }

    for (let button of deleteButtons){
        button.style.display = "block"
    }
}

//Hide buttons and display update form
function editItem(event) {
    let button = event.target
    let parent = button.parentElement
    parent.style.display = "none";
    let buttonClassItem = button.classList[0]
    
    for (let form of updateForms) {
        let formClassItem = form.classList[0]
        if(formClassItem == buttonClassItem){
            form.style.display ="inline-block"
        }
    }
}

// Button to display item buttons
if(editListButton){
    editListButton.addEventListener("click", showItemButtons)
}

// Buttons to display update form
if(editButtons) {
    for (let button of editButtons){
    button.addEventListener("click", editItem)
    }
}


//Edit list name
const editNameButton = document.getElementById("name-edit-button")
const editNameForm = document.getElementById("list-name-form")
if(editNameForm){
    editNameForm.style.display = "none";
}

function editListName() {
    editNameButton.style.display = "none";
    editNameForm.style.display = "block";
}

if(editNameButton) {
    editNameButton.addEventListener("click", editListName)
}

// Messages
let closeButton = document.getElementById("message-close")

function closeMessage(){
    messageDiv = document.getElementById("message-container")
    messageDiv.style.display = "none"
}

if(closeButton){
    closeButton.addEventListener("click", closeMessage)
}