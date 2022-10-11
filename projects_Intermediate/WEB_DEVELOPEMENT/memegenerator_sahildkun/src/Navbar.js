import React from 'react'
import './App.css'
import trollface from './images/Troll Face (1).png'
function Navbar() {
  return (
    <div className='' id='gradient'>
        <div className='flex flex-auto items-center space-x-5'>
    <img src={trollface} alt="" className='lg:h-14 lg:ml-10  lg:pt-2
    sd: h-7 m-3 
    ' />
    <h1 className='lg:text-xl text-white lg:font-serif
    sm: text-sm font-mono
    '>MeMe Generator</h1>
    <h2 className='flex  flex-auto justify-end pr-16 font-bold text-white'>Project</h2>
    </div>
    </div>
  )
}

export default Navbar