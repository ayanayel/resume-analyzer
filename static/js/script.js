document.addEventListener("DOMContentLoaded", () => {

  // --- Resume file upload: disable the paste box when a file is chosen ---
  const fileInput = document.getElementById("resume_file");
  const textArea = document.getElementById("resume_text");

  if (fileInput && textArea) {
    fileInput.addEventListener("change", () => {
      const hasFile = fileInput.files.length > 0;

      textArea.disabled = hasFile;
      textArea.placeholder = hasFile
        ? `Using uploaded file: ${fileInput.files[0].name}`
        : "Paste your resume text here...";

      textArea.style.opacity = hasFile ? "0.55" : "1";
    });
  }

  // --- Results page tabs: show one section at a time ---
  const tabButtons = document.querySelectorAll(".tab");
  const tabContents = document.querySelectorAll(".tab-content");

  tabButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const target = button.getAttribute("data-tab");

      tabButtons.forEach((b) => b.classList.remove("active"));
      button.classList.add("active");

      tabContents.forEach((content) => {
        content.style.display = (content.id === target) ? "block" : "none";
      });
    });
  });
});