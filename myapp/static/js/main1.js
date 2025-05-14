/ NAVBAR / 

const offcanvasElement = document.getElementById('mainNavbarOffcanvas');
  const toggler = document.getElementById('navbarToggler');

  function updateTogglerVisibility() {
    if (window.innerWidth >= 992) {
      // Desktop view
      toggler.style.display = 'none';
    } else {
      // Mobile view
      toggler.style.display = 'block';
    }
  }

  // Hide toggler when offcanvas opens
  offcanvasElement.addEventListener('show.bs.offcanvas', () => {
    toggler.style.display = 'none';
  });

  // Show toggler again when offcanvas closes
  offcanvasElement.addEventListener('hidden.bs.offcanvas', () => {
    updateTogglerVisibility();
  });

  // Also handle screen resize dynamically
  window.addEventListener('resize', updateTogglerVisibility);

  // Initial check on load
  window.addEventListener('DOMContentLoaded', updateTogglerVisibility);