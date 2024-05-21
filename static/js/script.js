//Delete list toast
const deleteListButton = document.getElementById('delete-list-button')
const deleteListToast = document.getElementById('deleteListToast')

if (deleteListButton){
    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(deleteListToast)
    deleteListButton.addEventListener('click', (e) => {
    toastBootstrap.show()
})
}

// Delete list confirmation modal
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
newListModalButton.addEventListener("click", showNewListModal )

// Edit item
const editButtons = document.getElementsByClassName("item-edit-button")
const updateForms = document.getElementsByClassName("item-edit-form")
for (let form of updateForms){
    form.style.display = "none"
}

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

if(editButtons) {
    for (let button of editButtons){
    button.addEventListener("click", editItem)
    }
}

//Edit list name
const editNameButton = document.getElementById("name-edit-button")
const editNameForm = document.getElementById("list-name-form")
editNameForm.style.display = "none";

function editListName() {
    editNameButton.style.display = "none";
    editNameForm.style.display = "block";

}

if(editNameButton) {
    editNameButton.addEventListener("click", editListName)
}