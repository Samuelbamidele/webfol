const dynamicText = document.getElementById("dynamic-text");
const roles = ["Freelancer", "Developer", "Technician"];
let currentRoleIndex = 0;
let letterIndex = 0;
let isDeleting = false;

function typeEffect() {
    const currentRole = roles[currentRoleIndex];
    if (isDeleting) {
        // Remove one letter at a time
        dynamicText.textContent = currentRole.slice(0, letterIndex--);
        if (letterIndex < 0) {
            isDeleting = false;
            currentRoleIndex = (currentRoleIndex + 1) % roles.length; // Move to next role
        }
    } else {
        // Add one letter at a time
        dynamicText.textContent = currentRole.slice(0, ++letterIndex);
        if (letterIndex === currentRole.length) {
            isDeleting = true;
            setTimeout(typeEffect, 1500); // Pause before deleting
            return;
        }
    }
    setTimeout(typeEffect, isDeleting ? 50 : 100);
}

// Start the typing effect
typeEffect();
