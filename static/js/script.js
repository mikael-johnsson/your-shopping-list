// Delete list confirmation modal
const deleteListButton = document.getElementById('delete-list-button');
/**
 * Function that displays the Delete List Modal when user clicks 
 * the delete list button in list_detail.html.
 * 
 */
function showDeleteListModal () {
    const deleteConfirmationModal = document.getElementById("delete-confirmation-modal");
    const modal = new bootstrap.Modal(deleteConfirmationModal);
    modal.show();
}


if (deleteListButton) {
    deleteListButton.addEventListener("click", showDeleteListModal);
}

// Clear list confirmation modal
const clearListButton = document.getElementById('clear-list-button');
/**
 * Function that displays the Clear List Modal when user clicks 
 * the clear list button in list_detail.html.
 * 
 */
function showClearListModal () {
    const clearConfirmationModal = document.getElementById("clear-confirmation-modal");
    const modal = new bootstrap.Modal(clearConfirmationModal);
    modal.show();
}


if (clearListButton) {
    clearListButton.addEventListener("click", showClearListModal);
}

// Share list modal
const shareListButton = document.getElementById("share-list-button");
/**
 * Function that displays the Share List Modal when user clicks 
 * the Share List button in list_detail.html
 */
function shareListModal () {
    const emailModal = document.getElementById("share-list-modal");
    const modal = new bootstrap.Modal(emailModal);
    modal.show();
}


if (shareListButton) {
    shareListButton.addEventListener("click", shareListModal);
}

// Share list function
/**
 * Function that lets the user send the list via EmailJS.
 * Via a form the function gathers the users name, the receivers email, 
 * a message and the list containing the list items.
 */
function sendMail (shareList) {
    let listName = document.getElementById("list-name");
    let listItemElements = document.getElementsByClassName("list-items");
    let listItemValues = [];
    for (let element of listItemElements) {
        let value = element.textContent;
        listItemValues.push(value);
    }

    emailjs.send("service_s8rbn75", "template_zvdv8q9", {
            "from_name": shareList.senderName.value,
            "to_email": shareList.emailInput.value,
            "list_name": listName.textContent,
            "list_items": listItemValues,
            "message": shareList.message.value
        })
        .then(
            function (response) {
                console.log("success", response);
            },
            function (error) {
                console.log("fail", error);
            }
        );

}


// Give new list a name modal
const newListModal = document.getElementById("new-list-modal");
/**
 * Function that displays the New List modal when user clicks 
 * Create New List button.
 */
function showNewListModal() {
    const modal = new bootstrap.Modal(newListModal);
    modal.show();
}


let newListModalButton = document.getElementById("create-list-button");
if (newListModalButton) {
    newListModalButton.addEventListener("click", showNewListModal);
}

// Edit items section//
const editListButton = document.getElementById("edit-list-button");
const editButtons = document.getElementsByClassName("item-edit-button");
const deleteButtons = document.getElementsByClassName("delete-item-button");
const updateForms = document.getElementsByClassName("item-edit-form");

//Hide item buttons and update forms
for (let button of editButtons) {
    button.style.display = "none";
}

for (let button of deleteButtons) {
    button.style.display = "none";
}
for (let form of updateForms) {
    form.style.display = "none";
}

/**
 * Function that toggles the displaying of the item edit and delete buttons
 * when the user clicks the Edit List button.
 */
function showItemButtons () {
    for (let button of editButtons) {
        if (button.style.display === "none") {
            button.style.display = "block";
        } else {
            button.style.display = "none";
        }
    }

    for (let button of deleteButtons) {
        if (button.style.display === "none") {
            button.style.display = "block";
        } else {
            button.style.display = "none";
        }
    }
}


/**
 * Function that hides the item edit and delete button of a certain item and 
 * shows the update item form whn user clicks the Edit button.
 */
function editItem (event) {
    let button = event.target;
    let parent = button.parentElement;
    parent.style.display = "none";
    let buttonClassItem = button.classList[0];

    for (let form of updateForms) {
        let formClassItem = form.classList[0];
        if (formClassItem == buttonClassItem) {
            form.style.display = "inline-block";
        }
    }
}


// Button to display item buttons
if (editListButton) {
    editListButton.addEventListener("click", showItemButtons);
}

// Buttons to display update form
if (editButtons) {
    for (let button of editButtons) {
        button.addEventListener("click", editItem);
    }
}

//Edit list name
const editNameButton = document.getElementById("name-edit-button");
const editNameForm = document.getElementById("list-name-form");
if (editNameForm) {
    editNameForm.style.display = "none";
}

/**
 * Function that hides the Edit List Name button and displays the 
 * Update List Name form when user clicks the Edit List Name button.
 */
function editListName () {
    editNameButton.style.display = "none";
    editNameForm.style.display = "block";
}


if (editNameButton) {
    editNameButton.addEventListener("click", editListName);
}

// Messages
let closeButton = document.getElementById("message-close");

/**
 * Function that stops displaying the message when the user clicks 
 * the Close Message button.
 */
function closeMessage() {
    let messageDiv = document.getElementById("message-container");
    messageDiv.style.display = "none";
}


if (closeButton) {
    closeButton.addEventListener("click", closeMessage);
}