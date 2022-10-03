import React from 'react'
import { Typography,Stack,Button } from '@mui/material'
import BodyPartImage from '../assets/icons/body-part.png'
import TargetImage from '../assets/icons/target.png'
import EquitmentImage from '../assets/icons/equipment.png'


const Detail = ({exerciseDetail}) => {


    const { bodyPart, gifUrl, name, target, equipment } = exerciseDetail
    
    const extraDetail = [
        {
            icon: BodyPartImage,
            name:bodyPart
        },
        {
            icon: TargetImage,
            name:target
        },
        {
            icon: EquitmentImage,
            name:equipment
        }
    ]

  return (
      <Stack gap='60px' sx={{
          flexDirection: { lg: 'row' },
          p: '20px',
          alignItems:'center'
      }}>
          <img src={gifUrl} alt={name} loading='lazy' className='detail-image' />
          <Stack sx={{
              gap:{lg:'35px',xs:'20px'}
          }}>
              <Typography sx={{ fontSize: { lg: '64px', xs: '30px' } }} fontWeight={700} textTransform="capitalize">
                  {name}
              </Typography>
              <Typography sx={{ fontSize: { lg: '24px', xs: '18px' } }} color="#4F4C4C" justifyContent='start'>
              Exercises keep you strong.{' '}
          <span style={{ textTransform: 'capitalize' }}>{name}</span> is one
          of the best exercises to target your {target}. It will help you improve your{' '}
          mood and gain energy.
              </Typography>
              {extraDetail.map((item, i) => (
                  <Stack key={i} direction='row' gap='24px' alignItems='center'>
                      <Button sx={{
                          background: '#fff2db',
                          borderRadius: '50%',
                          width: {lg:'90px',xs:'60px'},
                          height:{lg:'90px',xs:'60px'}
                      }}>
                          <img src={item.icon} alt={ bodyPart} style={{width:'40px',height:'40px'}} />
                      </Button>
                      <Typography textTransform="capitalize" sx={{ fontSize: { lg: '30px', xs: '18px' } }}>{item.name}</Typography>
                  </Stack>
              ))}
          </Stack>
    </Stack>
  )
}

export default Detail