//Delete list toast

const deleteListButton = document.getElementById('delete-list-button')
const deleteListToast = document.getElementById('deleteListToast')


if (deleteListButton){
    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(deleteListToast)
    deleteListButton.addEventListener('click', (e) => {
    toastBootstrap.show()
})
}

const newListModal = document.getElementsByClassName("modalShow")
if(newListModal){
    document.getElementById("new-list-modal").show();
}

