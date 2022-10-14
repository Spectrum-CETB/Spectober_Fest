import './App.css';
import React, { Component } from 'react';
import Generate from './Components/Generate';
                
class App extends Component {
  render() { 
    return (
      <div className='container'>
      <h1 className='tt'>Gotta Catch 'Em All</h1>
      <br/>
      <Generate />

      </div>
    );
  }
}
 
export default App;

