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
if(deleteListButton){ //if statement to avoid error in console of non existing variable
    deleteListButton.addEventListener("click", showDeleteListModal)
}
    

// Give new list a name modal
const newListModal = document.getElementById("new-list-modal")
if(newListModal){
    const modal = new bootstrap.Modal(newListModal);
    modal.show();
    
}

// Edit item
const editButtons = document.getElementsByClassName("item-edit-button")
const updateForms = document.getElementsByClassName("item-edit-form")
for (let form of updateForms){
    form.style.display = "none"
}

function editItem(event) {
    let parentDiv = event.target.parentElement
    parentDiv.style.display = "none";
    for (let form of updateForms){
        if(form.previousElementSibling.children[2] == event.target){
            form.style.display = "block";
        }
    }
    
    
}

if(editButtons) {
    for (let button of editButtons){
    button.addEventListener("click", editItem)
    }
}