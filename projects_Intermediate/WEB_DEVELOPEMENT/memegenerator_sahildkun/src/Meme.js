import React, { useState } from 'react'
import Data from './Data';
import './App.css'
function Meme() {

  const [memeImage , setMemeImage] = useState({

    firstName: "",
    secondName: "",
    randomImage:"https://i.pinimg.com/736x/48/54/c2/4854c2cd8f0e69be5d0dd124662654f2.jpg"
  });


  function handleChange(event){

    
   setMemeImage((prevState)=>(
   {
      ...prevState,
      [event.target.name]: [event.target.value]
    }
   ))
  }
  console.log(memeImage);

    function handleClick() {
        
        
        const datarray = Data.data.memes;
        const url = datarray[Math.floor(Math.random() * 101)].url;
         setMemeImage((prevState) => (
         {
             ...prevState,
             randomImage: url
          }
         ));
       
        
    }
  return (
    <>
    <div action="" className=' mt-10 bg-white
    rounded-md
    shadow-xl
    border
    mx-4
    border-purple-500
    sm:w-auto
    sm:shadow-md
    sm:border-purple-500
    sm:
    '>
    <div className='grid grid-cols-1 p-10  gap-5
    sm:grid-cols-2

    
    '>
        <input type="text"
        name='firstName'
        value={memeImage.firstName}
        onChange={handleChange}
        placeholder='enter first word' 
        className=' border-gray-400 border-2 
        rounded-md
        px-2
        focus:outline-none
        focus:border-purple-600
        
        
        '/>
        <input type="text" 
        name='secondName'
        onChange={handleChange}

        value={memeImage.secondName}
        placeholder='enter second word' 
        className=' border-gray-400 border-2 
        rounded-md
        px-2
        focus:outline-none
        focus:border-purple-600
        '/>
        <div className='grid  '>
        <button onClick={handleClick} className='bg-yellow-200  rounded
        border 
        
        my-5
        sm:bg-yellow-200
        sm:w-[89rem]
        sm:my-10
        '>
         GENERATE MEME
        </button>
    </div>
        
        
    </div>
   
    </div>
    <div className='flex flex-auto justify-center mb-14 mt-16
    
    
    '>
   
    
    <img src={memeImage.randomImage} alt="" className='w-[300px]
    h-[300px]
    sm:h-[20rem]
    w:w-auto
    
  
    ' />
    <h2 className='meme--text'
    id=''
    >{memeImage.firstName}</h2>
    <h2 className='meme--text bottom'id=''>{memeImage.secondName}</h2>
    
    </div>
   
    
    </>
  )
}

export default Meme