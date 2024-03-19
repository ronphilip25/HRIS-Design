
// Toggle submenus
document.addEventListener('DOMContentLoaded', function () {
  const toggleSubmenu = (btnId, submenuClass) => {
    const btn = document.getElementById(btnId);
    const submenu = document.querySelector(`.${submenuClass}`);

    btn.addEventListener('click', function () {
      submenu.style.display = submenu.style.display === 'none' ? 'block' : 'none';
    });
  };

  toggleSubmenu('dashboardBtn', 'dashboard-submenu');
  toggleSubmenu('attendanceBtn', 'attendance-submenu');
  toggleSubmenu('teamBtn', 'team-submenu');
  toggleSubmenu('leavesBtn', 'leaves-submenu');
  toggleSubmenu('filingBtn', 'filing-submenu');
  toggleSubmenu('settingsBtn', 'settings-submenu');
});

document.addEventListener('DOMContentLoaded', function () {
  const dashboardBtn = document.getElementById('dashboardBtn');

  dashboardBtn.addEventListener('click', function () {
    if (!dashboardBtn.classList.contains('active')) {
      dashboardBtn.classList.add('active');
    } else {
      dashboardBtn.classList.remove('active');
    }
  });
});

// Toggle attendance chart
document.addEventListener('DOMContentLoaded', function () {
    var ctx = document.getElementById('attendanceChart').getContext('2d');
    var gradient1 = ctx.createLinearGradient(0, 0, 0, 400);
    gradient1.addColorStop(0, 'rgba(54, 162, 235, 1)');
    gradient1.addColorStop(1, 'rgba(54, 162, 235, 0.2)');
  
    var gradient2 = ctx.createLinearGradient(0, 0, 0, 400);
    gradient2.addColorStop(0, 'rgba(255, 99, 132, 1)');
    gradient2.addColorStop(1, 'rgba(255, 99, 132, 0.2)');

    var gradient3 = ctx.createLinearGradient(0, 0, 0, 400);
    gradient3.addColorStop(0, 'rgba(75, 192, 192, 1)');
    gradient3.addColorStop(1, 'rgba(75, 192, 192, 0.2)');

    var gradient4 = ctx.createLinearGradient(0, 0, 0, 400);
    gradient4.addColorStop(0, 'rgba(153, 102, 255, 1)');
    gradient4.addColorStop(1, 'rgba(153, 102, 255, 0.2)');

    var hrisChart = new Chart(ctx, {
          type: 'line',
          data: {
              labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
              datasets: [{
                  label: 'Employees',
                  backgroundColor: gradient1,
                  borderColor: 'rgba(54, 162, 235, 1)',
                  borderWidth: 1,
                  data: [50, 45, 55, 60, 55, 65, 70, 75, 80, 85, 90, 95],
                  shadowColor: 'rgba(54, 162, 235, 0.5)',
                  shadowBlur: 10
              },
              {
                  label: 'Tardies',
                  backgroundColor: gradient2,
                  borderColor: 'rgba(255, 99, 132, 1)',
                  borderWidth: 1,
                  data: [5, 4, 6, 3, 7, 5, 4, 6, 3, 5, 4, 7],
                  shadowColor: 'rgba(255, 99, 132, 0.5)',
                  shadowBlur: 10
              },
              {
                  label: 'Official Business',
                  backgroundColor: gradient3,
                  borderColor: 'rgba(75, 192, 192, 1)',
                  borderWidth: 1,
                  data: [8, 9, 7, 10, 6, 8, 9, 7, 10, 8, 9, 6],
                  shadowColor: 'rgba(75, 192, 192, 0.5)',
                  shadowBlur: 10
              },
              {
                  label: 'Others',
                  backgroundColor: gradient4,
                  borderColor: 'rgba(153, 102, 255, 1)',
                  borderWidth: 1,
                  data: [10, 12, 8, 14, 9, 10, 12, 8, 14, 10, 12, 9],
                  shadowColor: 'rgba(153, 102, 255, 0.5)',
                  shadowBlur: 10
              }]
          },
          options: {
              animation: {
                  duration: 2000,
                  easing: 'easeInOutQuart'
              },
              scales: {
                  y: {
                      beginAtZero: true
                  }
              }
          }
      });
  });

// Toggle form 
    function toggleForm(showForm) {
        const formContainer = document.getElementById("formContainer");
        const expandableForm = document.getElementById("expandableForm");
        const outerSaveBtn = document.getElementById("outerSaveBtn");

        if (showForm) {
            formContainer.classList.remove("hidden");
            expandableForm.classList.add("row-span-2");
            outerSaveBtn.classList.add("hidden");
        } else {
            formContainer.classList.add("hidden");
            expandableForm.classList.remove("row-span-2");
            outerSaveBtn.classList.remove("hidden");
        }
    }

    function toggleForm1(showForm1) {
        const formContainer1 = document.getElementById("formContainer1");
        const expandableForm1 = document.getElementById("expandableForm1");
        const outerSaveBtn1 = document.getElementById("outerSaveBtn1");

        if (showForm1) {
            formContainer1.classList.remove("hidden");
            expandableForm1.classList.add("row-span-2");
            outerSaveBtn1.classList.add("hidden");
        } else {
            formContainer1.classList.add("hidden");
            expandableForm1.classList.remove("row-span-2");
            outerSaveBtn1.classList.remove("hidden");
        }
    }

// Dropdown
function toggleDropdown() {
  var dropdownMenu = document.getElementById("dropdown-menu");
  var menuButton = document.getElementById("menu-button");
  var isExpanded =
    menuButton.getAttribute("aria-expanded") === "true";
  if (isExpanded) {
    dropdownMenu.classList.add("hidden");
    menuButton.setAttribute("aria-expanded", "false");
  } else {
    dropdownMenu.classList.remove("hidden");
    menuButton.setAttribute("aria-expanded", "true");
  }
}

// Dropdown2
function toggleDropdown() {
    var dropdownMenu = document.getElementById("dropdown-menu");
    var menuButton = document.getElementById("menu-button");
    var isExpanded = menuButton.getAttribute("aria-expanded") === "true";

    if (isExpanded) {
      dropdownMenu.classList.add("hidden");
      menuButton.setAttribute("aria-expanded", "false");
    } else {
      dropdownMenu.classList.remove("hidden");
      menuButton.setAttribute("aria-expanded", "true");
    }
  }


// Clickable Icon
const button = document.getElementById('company-info-btn');
    const text = document.getElementById('company-info-btn');
    const svg = document.getElementById('clickable-icon');

    button.addEventListener('click', function() {
        // Add blue color to text
        text.classList.add('blue-text');
        // Add blue color to SVG
        svg.classList.add('blue-svg');
    });