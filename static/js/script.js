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

