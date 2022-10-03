import React from 'react'
import {BrowserRouter as Router,Routes,Route} from 'react-router-dom'
import { Layout} from 'antd'
import { Provider } from 'react-redux'
import store from './app/store'
import { Navbar,Exchanges,Homepage,Cryptocurrencies,CryptoDetails,News,Footer } from './components'
import './App.css'
const App = () => {
    return (
        <Router>
            <Provider store={store}>
      <div className="app">
          <div className="navbar">
              <Navbar/>
          </div>
          <div className="main">
                    <Layout>
                        <div className="routes">
                            <Routes>
                                <Route exact path='/' element={<Homepage/>}>
                                </Route>
                                <Route exact path='/exchanges' element={<Exchanges/>}>
                                    
                                </Route>
                                <Route exact path='/cryptocurrencies' element={<Cryptocurrencies/>}>
                                    
                                </Route>
                                <Route exact path='/crypto/:coinId' element={<CryptoDetails/>}>
                                    
                                </Route>
                                <Route exact path='/news' element={<News/>}>
                                    
                                </Route>
                            </Routes>
                        </div>
              </Layout>
          
          <div className="footer" >
                    <Footer/>
                    </div>
                    </div>
                </div>
                </Provider>
        </Router>
  )
}

export default App