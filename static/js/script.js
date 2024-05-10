//Delete list toast

const deleteListButton = document.getElementById('delete-list-button')
const deleteListToast = document.getElementById('deleteListToast')
console.log(deleteListButton)

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
deleteListButton.addEventListener("click", showDeleteListModal)
    

// Give new list a name modal
const newListModal = document.getElementById("new-list-modal")
if(newListModal){
    const modal = new bootstrap.Modal(newListModal);
    modal.show();
    
}

