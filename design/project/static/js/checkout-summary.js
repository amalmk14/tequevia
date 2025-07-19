// web

document.getElementById('saveWebAddress').addEventListener('click', function () {
    const name = document.querySelector('input[placeholder="Name"]').value;
    const city = document.querySelector('input[placeholder="City/District/Town"]').value;
    const locality = document.querySelector('input[placeholder="Locality"]').value;
    const state = document.querySelector('select.form-select').value;
    const pincode = document.querySelector('input[placeholder="Pincode"]').value;

    const fullAddress = `${locality}, ${city}, ${state} - ${pincode}`;

    // Set summary at top
    document.getElementById('summaryName').textContent = name;
    document.getElementById('summaryAddress').textContent = fullAddress;

    // Set final saved address at bottom
    document.getElementById('finalName').textContent = name;
    document.getElementById('finalAddress').textContent = fullAddress;
    document.getElementById('finalSavedAddress').classList.remove('d-none');

    // Hide address form and show summary
    document.getElementById('webAddressForm').classList.add('d-none');
    document.getElementById('webAddressSavedSummary').classList.remove('d-none');
    document.getElementById('changeAddressBtn').classList.remove('d-none');

    //  Expand ORDER SUMMARY
    document.getElementById('orderSummaryBlock').classList.remove('d-none');
  });

  document.getElementById('changeAddressBtn').addEventListener('click', function () {
    // Show address form again
    document.getElementById('webAddressForm').classList.remove('d-none');
    document.getElementById('webAddressSavedSummary').classList.add('d-none');
    document.getElementById('changeAddressBtn').classList.add('d-none');

    // Hide saved address summary
    document.getElementById('finalSavedAddress').classList.add('d-none');

    //  Collapse ORDER SUMMARY
    document.getElementById('orderSummaryBlock').classList.add('d-none');
  });

  

// mobile

  const mobileForm = document.getElementById('mobileAddressForm');
  const mName = document.getElementById('mName');
  const mPincode = document.getElementById('mPincode');
  const mState = document.getElementById('mState');
  const mCity = document.getElementById('mCity');
  const mHouse = document.getElementById('mHouse');
  const mArea = document.getElementById('mArea');

  mobileForm.addEventListener('submit', function (e) {
    e.preventDefault();

    // Build address string
    const address = `${mHouse.value}, ${mArea.value}, ${mCity.value}, ${mState.value} - ${mPincode.value}`;
    const name = mName.value;

    // Update summary
    document.getElementById('mobileSummaryName').innerText = name;
    document.getElementById('mobileSummaryAddress').innerText = address;

    // Toggle visibility
    document.querySelector('.mobile-checkout').classList.add('d-none');
    document.getElementById('deliverySection').classList.remove('d-none');
    document.getElementById('orderSummarySection').classList.remove('d-none');
  });

  document.getElementById('changeMobileAddressBtn').addEventListener('click', () => {
    document.querySelector('.mobile-checkout').classList.remove('d-none');
    document.getElementById('deliverySection').classList.add('d-none');
    document.getElementById('orderSummarySection').classList.add('d-none');
  });