function showToast(title, message, type = "normal", duration = 3000) {
  const toastComponent = document.getElementById("toast-component");
  const toastTitle = document.getElementById("toast-title");
  const toastMessage = document.getElementById("toast-message");
  const toastIcon = document.getElementById("toast-icon");

  if (!toastComponent || !toastTitle || !toastMessage || !toastIcon) return;

  // Remove existing classes
  toastComponent.classList.remove(
    "bg-red-50", "border-red-500", "text-red-600",
    "bg-green-50", "border-green-500", "text-green-600",
    "bg-blue-50", "border-blue-500", "text-blue-600",
    "bg-yellow-50", "border-yellow-500", "text-yellow-600"
  );

  // Set type-specific styling and icon
  let bgColor, borderColor, textColor, icon;
  switch (type) {
    case "success":
      bgColor = "bg-green-50";
      borderColor = "border-green-500";
      textColor = "text-green-600";
      icon = "✓";
      break;
    case "error":
      bgColor = "bg-red-50";
      borderColor = "border-red-500";
      textColor = "text-red-600";
      icon = "✕";
      break;
    case "warning":
      bgColor = "bg-yellow-50";
      borderColor = "border-yellow-500";
      textColor = "text-yellow-600";
      icon = "⚠";
      break;
    default:
      bgColor = "bg-blue-50";
      borderColor = "border-blue-500";
      textColor = "text-blue-600";
      icon = "ℹ";
  }

  // Apply classes
  toastComponent.classList.add(bgColor, borderColor, textColor);

  // Set content
  toastTitle.textContent = title;
  toastMessage.textContent = message;
  toastIcon.textContent = icon;

  // Show toast
  toastComponent.classList.remove("opacity-0", "translate-y-64");
  toastComponent.classList.add("opacity-100", "translate-y-0");

  // Auto hide after duration
  setTimeout(() => {
    toastComponent.classList.remove("opacity-100", "translate-y-0");
    toastComponent.classList.add("opacity-0", "translate-y-64");
  }, duration);
}
