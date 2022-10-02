import React from 'react'
import { Box, Stack, Typography } from "@mui/material";
import Logo from '../assets/images/fitbytes2.png'
import { FaInstagram, FaLinkedin, FaTwitter } from "react-icons/fa";


const Footer = () => {
  return (
    <Box mt="80px" bgcolor="#FFF3F4">
      <Stack gap="5px" sx={{ alignItems: 'center' }} flexWrap="wrap" px="40px" pt="28px"> 
        <img src={Logo} alt="logo" style={{ width: '200px', height: '32px' }} />
        <Typography variant="h5" fontWeight={600} sx={{ fontSize: { lg: '18px', xs: '18px' } }} mt="10px" textAlign="center" pb="12px">
          Made with 💪 by Prateek Rath
        </Typography>
        <Typography gap="20px" sx={{
          flexDirection: 'row',
          justifyContent: 'center',
          gap: '20px',
          paddingBottom: '30px',
          fontSize:'20px'
        }}>
        <a className='footer-link'  href="https://www.linkedin.com/in/prateek-rath-9a9779219/">
          <FaLinkedin />
        </a>
        <a className='footer-link' href="https://twitter.com/iampsr8">
          <FaTwitter />
        </a>
        <a className='footer-link' href="https://www.instagram.com/i_am_psr8/">
          <FaInstagram />
        </a>
        </Typography>
      </Stack>
      
    </Box>
  )
}

export default Footer