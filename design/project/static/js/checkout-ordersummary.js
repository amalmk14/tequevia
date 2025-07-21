document.getElementById('saveAddress').addEventListener('click', function () {
    const name = document.querySelector('input[placeholder="Name"]').value;
    const city = document.querySelector('input[placeholder="City/District/Town"]').value;
    const locality = document.querySelector('input[placeholder="Locality"]').value;
    const state = document.querySelector('select.form-select').value;
    const pincode = document.querySelector('input[placeholder="Pincode"]').value;

    // Validate required fields
    if (!name || !city || !locality || !state || !pincode) {
        alert('Please fill in all required fields');
        return;
    }

    const fullAddress = `${locality}, ${city}, ${state} - ${pincode}`;

    // Set summary
    document.getElementById('summaryName').textContent = name;
    document.getElementById('summaryAddress').textContent = fullAddress;

    // Hide address form and show summary
    document.getElementById('addressForm').classList.add('d-none');
    document.getElementById('addressSavedSummary').classList.remove('d-none');
    document.getElementById('changeAddressBtn').classList.remove('d-none');

    // Show order summary
    document.getElementById('orderSummaryBlock').classList.remove('d-none');
});

document.getElementById('changeAddressBtn').addEventListener('click', function () {
    // Show address form again
    document.getElementById('addressForm').classList.remove('d-none');
    document.getElementById('addressSavedSummary').classList.add('d-none');
    document.getElementById('changeAddressBtn').classList.add('d-none');

    // Hide order summary
    document.getElementById('orderSummaryBlock').classList.add('d-none');
});

// Quantity control functionality
document.addEventListener('click', function(e) {
    if (e.target.textContent === '+') {
        const qtySpan = e.target.previousElementSibling;
        const currentQty = parseInt(qtySpan.textContent);
        qtySpan.textContent = currentQty + 1;
    } else if (e.target.textContent === '-') {
        const qtySpan = e.target.nextElementSibling;
        const currentQty = parseInt(qtySpan.textContent);
        if (currentQty > 1) {
            qtySpan.textContent = currentQty - 1;
        }
    } else if (e.target.classList.contains('remove-btn')) {
        if (confirm('Are you sure you want to remove this item?')) {
            e.target.closest('.product').remove();
        }
    }
});