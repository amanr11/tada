function openModal() {
    document.getElementById("addAssessmentModal").style.display = "block";
}

function closeModal() {
    document.getElementById("addAssessmentModal").style.display = "none";
}

document.addEventListener("DOMContentLoaded", function() {
    const flashes = document.querySelector('.flashes');
    if (flashes) {
        setTimeout(() => {
            flashes.classList.add('fade-out');
            setTimeout(() => {
                flashes.style.display = 'none';
            }, 500);
        }, 500);
    }
});

function redirectToAddAssessment() {
    const title = document.getElementById("todoText").value;
    const url = addAssessmentUrl; // Use the URL variable from the top script
    console.log(url); // Debugging line to check the URL
    window.location.href = `${url}?title=${encodeURIComponent(title)}`;
}

function toggleDropdown() {
    document.getElementById("dropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
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

// Function to submit the form on Enter key press
document.getElementById("todoText").addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();  // Prevent the default form submission
        redirectToAddAssessment();  // Call the function to add the assessment
    }
});

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
