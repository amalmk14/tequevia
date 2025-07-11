// mobile view

const submenuData = {
    'current-season': {
        title: 'Current Season',
        items: [
            'View All',
            'New in Current Season',
            'End of Season Clearance'
        ]
    },
    'clearance': {
        title: 'Clearance',
        items: [
            'All Clearance Items',
            'Up to 50% Off',
            'Up to 70% Off',
            'Final Sale'
        ]
    },
    'fifa-world-cup': {
        title: 'FIFA World Cup',
        items: [
            'All World Cup Items',
            'National Teams',
            'Official Merchandise',
            'Collectibles'
        ]
    },
    'premier-league': {
        title: 'Premier League',
        items: [
            'All Premier League',
            'Manchester United',
            'Manchester City',
            'Liverpool',
            'Chelsea',
            'Arsenal'
        ]
    },
    'laiga': {
        title: 'La Liga',
        items: [
            'All La Liga',
            'Real Madrid',
            'Barcelona',
            'Atletico Madrid',
            'Valencia'
        ]
    },
    'national': {
        title: 'National',
        items: [
            'All National Teams',
            'England',
            'Spain',
            'Germany',
            'France',
            'Brazil',
            'Argentina'
        ]
    }
};

function toggleMobileMenu() {
    document.getElementById("mobileSideMenu").classList.toggle("active");
    document.getElementById("mobileMenuOverlay").classList.toggle("active");
    
    // Hide submenu if it's open
    if (document.getElementById("submenu").classList.contains("active")) {
        hideSubmenu();
    }
}

// New function for main menu items that should hide submenu
function selectMainMenuItem(element) {
    // Remove active class from all items
    document.querySelectorAll('.mobile-side-menu ul li').forEach(li => li.classList.remove('active'));
    
    // Add active class to clicked item
    element.parentElement.classList.add('active');
    
    // Hide submenu if it's open and return main menu to right side
    if (document.getElementById("submenu").classList.contains("active")) {
        hideSubmenu();
    }
    
    console.log('Selected main menu item:', element.textContent.trim());
}

// Keep the original function for items that don't have submenus
function selectMenuItem(element) {
    // Remove active class from all items
    document.querySelectorAll('.mobile-side-menu ul li').forEach(li => li.classList.remove('active'));
    
    // Add active class to clicked item
    element.parentElement.classList.add('active');
}

function showSubmenu(submenuType, element) {
    // Set active state for the clicked item
    selectMenuItem(element);
    
    // Get submenu data
    const data = submenuData[submenuType];
    
    // Update submenu title
    document.getElementById('submenuTitle').textContent = data.title;
    
    // Clear existing items
    const submenuItems = document.getElementById('submenuItems');
    submenuItems.innerHTML = '';
    
    // Add new items
    data.items.forEach(item => {
        const li = document.createElement('li');
        const a = document.createElement('a');
        a.href = '#';
        a.textContent = item;
        a.onclick = function() {
            console.log('Selected:', item);
            // You can add navigation logic here
        };
        li.appendChild(a);
        submenuItems.appendChild(li);
    });
    
    // Show submenu and move main menu to left
    document.getElementById('submenu').classList.add('active');
    document.getElementById('mobileSideMenu').classList.add('submenu-open');
}

function hideSubmenu() {
    document.getElementById('submenu').classList.remove('active');
    document.getElementById('mobileSideMenu').classList.remove('submenu-open');
}

// Close menu when clicking outside
document.addEventListener('click', function(event) {
    const menu = document.getElementById('mobileSideMenu');
    const submenu = document.getElementById('submenu');
    const toggle = document.querySelector('.mobile-menu-toggle');
    
    if (!menu.contains(event.target) && !submenu.contains(event.target) && !toggle.contains(event.target)) {
        if (menu.classList.contains('active')) {
            toggleMobileMenu();
        }
        if (submenu.classList.contains('active')) {
            hideSubmenu();
        }
    }
});



// web view

const webSubmenuData = {
  'new-in': ['New Collection', 'Latest Arrivals'],
  'recent-drops': ['Yesterday', 'Last 7 Days'],
  'classic': ['Retro Jerseys', 'Vintage Collectibles'],
  'current-season': ['View All', 'New Items', 'Clearance Sale'],
  'clearance': ['All Items', '50% Off', '70% Off', 'Final Sale'],
  'fifa-world-cup': ['Official Jerseys', 'Accessories', 'Souvenirs'],
  'premier-league': ['Arsenal', 'Chelsea', 'Liverpool'],
  'laiga': ['Real Madrid', 'Barcelona', 'Atletico Madrid'],
  'national': ['Brazil', 'Argentina', 'France']
};

function toggleWebMenu() {
  const menu = document.getElementById("webSideMenu");
  const submenu = document.getElementById("webSubmenu");
  menu.classList.toggle("active");
  if (!menu.classList.contains("active")) {
    submenu.classList.remove("active");
  }
}

function showWebSubmenu(key, element) {
  // Highlight active item
  document.querySelectorAll("#webSideMenu ul li").forEach(li => li.classList.remove('active'));
  element.parentElement.classList.add('active');

  // Populate submenu
  const data = webSubmenuData[key] || [];
  const submenuList = document.getElementById("webSubmenuItems");
  const title = document.getElementById("webSubmenuTitle");

  title.textContent = element.textContent.trim();
  submenuList.innerHTML = '';

  data.forEach(item => {
    const li = document.createElement("li");
    const a = document.createElement("a");
    a.href = "#";
    a.textContent = item;
    li.appendChild(a);
    submenuList.appendChild(li);
  });

  // Show submenu
  document.getElementById("webSubmenu").classList.add("active");
}


function selectWebMainItem(element) {
  // Remove active from all main items
  document.querySelectorAll("#webSideMenu ul li").forEach(li => li.classList.remove("active"));
  
  // Set active class
  element.parentElement.classList.add("active");

  // Hide submenu if it is open
  const submenu = document.getElementById("webSubmenu");
  submenu.classList.remove("active");
}


// top navbar scroll web and mobile


document.addEventListener("DOMContentLoaded", () => {
    const ul = document.getElementById("rollingNav");
    ul.innerHTML += ul.innerHTML; // clone items once
});