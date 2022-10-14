const imageContainer = document.getElementById('imageContainer');
const loader = document.getElementById('loader');

let ready = false;
let imagesLoaded = 0;
let totalImages = 0;
let photosArray = [];

let count = 30;
const apiKey = 'GWIMEr1vRYP-jF9MWNFwytHHrOAFIxprib2wjEmCEpM';
let apiUrl = `https://api.unsplash.com/photos/random/?client_id=${apiKey}&count=${count}`

function imageLoaded(){
  imagesLoaded++;
  console.log(imagesLoaded)
  if(imagesLoaded===totalImages){
  ready=true;
  loader.remove();
  }
}

function setAttributes(element, attributes){
  for(const key in attributes){
    element.setAttribute(key,attributes[key]);
  }
}

function displayPhotos(){
  imagesLoaded=0;
  totalImages = photosArray.length;
  photosArray.forEach((photo)=>{
    const item = document.createElement('a');
    // item.setAttribute('href',photo.links.html);
    // item.setAttribute('target','_blank');
    setAttributes(item,{
      href:photo.links.html,
      target:'_blank',
    })

    const img = document.createElement('img');
    // img.setAttribute('src',photo.urls.regular);
    // img.setAttribute('alt', photo.alt_description);
    // img.setAttribute('title', 'Click to redirect to Unsplash');
    setAttributes(img,{
      src:photo.urls.regular,
      alt:photo.alt_description,
      title:'Click to redirect to Unsplash'
    })

    img.addEventListener('load',imageLoaded);

    item.appendChild(img);
    imageContainer.appendChild(item);
  });
}

async function getPhotos(){
    try{
       const response = await fetch(apiUrl);
       photosArray = await response.json();
       displayPhotos();

    }catch(err){
      console.log(err);
    }
}

window.addEventListener('scroll',()=>{
  if(window.innerHeight+window.scrollY>=document.body.offsetHeight-1000 && ready){
    ready=false;
    getPhotos();
  }
})

getPhotos();