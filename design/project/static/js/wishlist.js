

  /* MOBILE bottom‑sheet */
  let mobileId=null;
  const ovM   =document.getElementById('mOverlay');
  const shM   =document.getElementById('mSheet');
  document.querySelectorAll('.m-card__more').forEach(btn=>{
    btn.addEventListener('click',e=>{
      mobileId=e.currentTarget.dataset.id;
      ovM.classList.add('show'); shM.classList.add('show');
    });
  });
  ovM.addEventListener('click',()=>{ovM.classList.remove('show');shM.classList.remove('show');mobileId=null});
  document.getElementById('mRemove').addEventListener('click',()=>{
    if(mobileId) document.querySelector(`.m-card[data-id='${mobileId}']`)?.remove();
    ovM.classList.remove('show'); shM.classList.remove('show');
  });
  
  /* DESKTOP delete */
  document.querySelectorAll('.d-item__del').forEach(b=>b.addEventListener('click',e=>{
    e.currentTarget.closest('.d-item').remove();
  }));
  
  /* shared */
  function addToCart(id){alert(`Added ${id} to cart (demo)`);}