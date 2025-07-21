 function toggleExpand(card) {
    const section = card.querySelector('.expand-section');
    section.style.display = section.style.display === 'block' ? 'none' : 'block';
  }

  function openSizeChangeModal(button) {
    const modal = document.getElementById('sizeChangeModal');
    const orderCard = button.closest('.order-card');
    
    // Get order details
    const productName = orderCard.querySelector('.order-title').textContent;
    const productColor = orderCard.querySelector('.order-color').textContent;
    const productImage = orderCard.querySelector('img').src;
    const deliveryDate = orderCard.querySelector('.order-status').textContent.replace('● ', '');
    
    // Extract current size from color info
    const currentSizeMatch = productColor.match(/Size:\s*(\w+)/);
    const currentSize = currentSizeMatch ? currentSizeMatch[1] : 'M';
    
    // Update modal content
    document.getElementById('modalProductName').textContent = productName;
    document.getElementById('modalProductColor').textContent = productColor.split('|')[0].trim();
    document.getElementById('modalCurrentSize').textContent = `Current Size: ${currentSize}`;
    document.getElementById('modalProductImage').src = productImage;
    document.getElementById('modalOrderDate').textContent = deliveryDate;
    
    // Disable current size option
    const sizeOptions = document.querySelectorAll('.size-option');
    sizeOptions.forEach(option => {
      option.classList.remove('disabled');
      if (option.textContent === currentSize) {
        option.style.opacity = '0.5';
        option.style.pointerEvents = 'none';
      } else {
        option.style.opacity = '1';
        option.style.pointerEvents = 'auto';
      }
    });
    
    // Reset form
    document.getElementById('sizeChangeForm').reset();
    document.getElementById('selectedSize').value = '';
    sizeOptions.forEach(option => option.classList.remove('selected'));
    
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }

  function closeSizeChangeModal() {
    const modal = document.getElementById('sizeChangeModal');
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
  }

  function selectSize(element, size) {
    // Remove previous selection
    document.querySelectorAll('.size-option').forEach(option => {
      option.classList.remove('selected');
    });
    
    // Add selection to clicked element
    element.classList.add('selected');
    document.getElementById('selectedSize').value = size;
  }

  function submitSizeChange(event) {
    event.preventDefault();
    
    const formData = {
      reason: document.getElementById('sizeChangeReason').value,
      newSize: document.getElementById('selectedSize').value,
      comments: document.getElementById('comments').value,
      contactNumber: document.getElementById('contactNumber').value,
      productName: document.getElementById('modalProductName').textContent,
      currentSize: document.getElementById('modalCurrentSize').textContent
    };
    
    // Here you would typically send this data to your backend
    console.log('Size Change Request:', formData);
    
    // Show success message
    alert('Size change request submitted successfully! Our team will contact you within 24 hours.');
    
    closeSizeChangeModal();
  }

  // Close modal when clicking outside
  document.getElementById('sizeChangeModal').addEventListener('click', function(event) {
    if (event.target === this) {
      closeSizeChangeModal();
    }
  });

  // Close modal with Escape key
  document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
      closeSizeChangeModal();
    }
  });