document.addEventListener('DOMContentLoaded', function(){})

async function vooData(){
  try {
    const response = await fetch('/voo/api');
    const data = await response.json();
    document.getElementById('vooprice').textContent = `VOO Price: ${data.close_value}`;
    document.getElementById('voodate').textContent = `Last Updated: ${data.close_date}`;
  } catch (error) {
    console.error('Error fetching stock data:', error);
  }
}

window.onload = vooData;

function changePage(sectorIndex, direction) {
  const page1 = document.getElementById(`page1_${sectorIndex}`);
  const page2 = document.getElementById(`page2_${sectorIndex}`);
  const page3 = document.getElementById(`page3_${sectorIndex}`);

  if (direction === 'graph') {
    page1.style.display = 'block';
    page2.style.display = 'none';
    page3.style.display = 'none';
  } else if (direction === 'table') {
    page1.style.display = 'none';
    page2.style.display = 'block';
    page3.style.display = 'none';
    // Initialize DataTables only if it hasn't been initialized yet
    $('.hover:visible').each(function () {
      if (!$.fn.DataTable.isDataTable(this)) {
        $(this).DataTable();
      }
    });
  } else if (direction === 'map') {
    page1.style.display = 'none';
    page2.style.display = 'none';
    page3.style.display = 'block';
  }
}

// Function to initialize DataTables for the initial page
function initializeDataTables() {
  $('.hover:visible').each(function() {
      if (!$.fn.DataTable.isDataTable(this)) {
          $(this).DataTable();
      }
  });
}

$(document).ready(function() {
  // Initialize DataTables for the initial page
  initializeDataTables();
}
);

