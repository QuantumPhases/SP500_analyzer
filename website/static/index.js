function changePage(sectorIndex, direction) {
    const page1 = document.getElementById(`page1_${sectorIndex}`);
    const page2 = document.getElementById(`page2_${sectorIndex}`);
  
    if (direction === 'next') {
      page1.style.display = 'none';
      page2.style.display = 'block';
    } else if (direction === 'prev') {
      page1.style.display = 'block';
      page2.style.display = 'none';
    }
  }