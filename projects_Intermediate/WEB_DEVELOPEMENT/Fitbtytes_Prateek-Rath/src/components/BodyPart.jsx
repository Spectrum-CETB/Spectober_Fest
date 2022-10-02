import React from 'react'
import { Stack, Typography } from '@mui/material'

import Icon from '../assets/icons/gym.png'

const BodyPart = ({ item, setBodyPart, bodyPart }) => {
    console.log(bodyPart)
    return (
      <Stack
            type="button"
            alignItems='center'
            justifyContent='center'
            className='bodyPart-card'
            sx={{
                    borderTop: bodyPart === item?'4px solid #ff2625':'',
                    background: '#fff',
                    borderBottomLeftRadius: '20px',
                    width: {lg:'270px',xs:'100px'},
                    height: {lg:'280px',xs:'140px'},
                    cursor: 'pointer',
                gap: { lg: '47px', xs:'30px'}
            }}
            onClick={() => {
                setBodyPart(item)
                window.scrollTo({top:'1800',left:100,behavior:'smooth'})
            }}
            
      >
          <img src={Icon} alt="dumbell" style={{
              width: '40px',
              height:'40px'
            }} />
            <Typography sx={{fontSize:{lg:'24px',xs:'18px'}}} fontWeight='bold' color='#3a1212' textTransform='capitalize' textAlign='center'>
                {item}
            </Typography>
    </Stack>
  )
}

export default BodyPart