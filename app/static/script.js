//flashes
document.addEventListener("DOMContentLoaded", function() {
    const flashes = document.querySelector('.flashes');
    if (flashes) {
        setTimeout(() => {
            flashes.classList.add('fade-out');
            setTimeout(() => {
                flashes.style.display = 'none';
            }, 500);
        }, 2000);
    }
});

//homepage assessment add
function redirectToAddAssessment() {
    const title = document.getElementById("todoText").value;
    const url = addAssessmentUrl; // Use the url variable from the program
    console.log(url); // Debugging line to check the url
    window.location.href = `${url}?title=${encodeURIComponent(title)}`;
}


//filter dropdown menu
function toggleDropdown() {
    document.getElementById("dropdown").classList.toggle("show");
}


window.onclick = function(event) {
    if (!event.target.matches('.filter-options button')) {
        const dropdowns = document.getElementsByClassName("dropdown-content");
        for (let i = 0; i < dropdowns.length; i++) {
            const openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

//enabling enter key as input
document.getElementById("todoText").addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();  // Prevent the default form submission
        redirectToAddAssessment();  // Call the function to add the assessment
    }
});

//form validation
function validateForm() {
    const title = document.getElementById("title").value;
    const moduleCode = document.getElementById("module_code").value;
    const deadlineDate = document.getElementById("deadline_date").value;

    if (!title) {
        alert("Title is required.");
        return false;
    }
    if (!moduleCode) {
        alert("Module code is required.");
        return false;
    }
    if (!deadlineDate) {
        alert("Deadline date is required.");
        return false;
    }
    return true;
}
