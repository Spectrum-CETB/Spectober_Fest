import React from 'react'
import { BrowserRouter as Router,Routes,Route } from 'react-router-dom'
import { Box } from '@mui/material'
import './App.css';
import Home from './pages/Home'
import ExerciseDetail from './pages/ExerciseDetail'
import Navbar from './components/Navbar'
import Footer from './components/Footer'

const App = () => {
    return (
      <Router>
      <Box width='400px' sx={{width:{xl:'1488px'}}} m='auto'>
          <Navbar/>
          <Routes>
                    <Route path='/' exact element={<Home />} />
                    <Route path='/exercise/:id' element={ <ExerciseDetail/>} />
          </Routes>
        <Footer/>
        </Box>
            </Router>
  )
}

export default App