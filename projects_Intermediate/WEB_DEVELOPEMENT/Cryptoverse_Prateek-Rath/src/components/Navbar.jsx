import React,{useState,useEffect} from 'react'
import {Button,Menu,Typography,Avatar} from 'antd'
import { Link } from 'react-router-dom'
import {HomeOutlined,MoneyCollectOutlined,BulbOutlined,FundOutlined,MenuOutlined} from '@ant-design/icons'
import icon from '../images/brilliantlogo.png'

const Navbar = () => {
    const [activeMenu, setActiveMenu] = useState(true)
    const [screenSize, setScreenSize] = useState(null)
    useEffect(() => {
        const handleResize=()=>setScreenSize(window.innerWidth)
        window.addEventListener('resize',handleResize)
        handleResize()
        return ()=>window.removeEventListener('resize',handleResize)
    },[])
    
    useEffect(() => {
        if (screenSize < 768) {
            setActiveMenu(false)
        } else {
            setActiveMenu(true)
        }
    },[screenSize])

  return (
      <div className="nav-container">
          <div className="logo-container">
              <Avatar src={icon} size="large" />
              <h2 className="logo custom">
                  <Link to="/" className='custom'>Cryptoverse</Link>
              </h2>
              <Button className='menu-control-container' onClick={()=>setActiveMenu(!activeMenu)}>
                  <MenuOutlined/>
              </Button>
          </div>
              {activeMenu && (
                  <Menu theme='dark'>
                  <Menu.Item icon={<HomeOutlined />}>
                      <Link to='/' onClick={()=>(screenSize<768 && setActiveMenu(!activeMenu))}>Home</Link>
                  </Menu.Item>
                  <Menu.Item icon={<FundOutlined />}>
                      <Link to='/cryptocurrencies' onClick={()=>(screenSize<768 && setActiveMenu(!activeMenu))}>Cryptocurrencies</Link>
                  </Menu.Item>
                  <Menu.Item icon={<MoneyCollectOutlined />}>
                      <Link to='/exchanges' onClick={()=>(screenSize<768 && setActiveMenu(!activeMenu))}>Exchanges</Link>
                  </Menu.Item>
                  <Menu.Item icon={<BulbOutlined />}>
                      <Link to='/news' onClick={()=>(screenSize<768 && setActiveMenu(!activeMenu))}>News</Link>
                  </Menu.Item>
              </Menu>
              )}
          
    </div>
  )
}

export default Navbar