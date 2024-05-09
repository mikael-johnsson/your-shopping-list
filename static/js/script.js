//Delete list toast
console.log('script.js loaded')

const deleteListButton = document.getElementById('delete-list-button')
const deleteListToast = document.getElementById('deleteListToast')


if (deleteListButton){
    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(deleteListToast)
    deleteListButton.addEventListener('click', (e) => {
    toastBootstrap.show()
})
}

const newListModal = document.getElementById("new-list-modal")
if(newListModal){
    const modal = new bootstrap.Modal(newListModal);
    modal.show();
    
}

