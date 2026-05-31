// WanderBG — Main JS

// Auto-dismiss alerts
document.addEventListener('DOMContentLoaded', function () {
  setTimeout(() => {
    document.querySelectorAll('.alert').forEach(el => {
      const bsAlert = new bootstrap.Alert(el);
      bsAlert.close();
    });
  }, 4000);
});
