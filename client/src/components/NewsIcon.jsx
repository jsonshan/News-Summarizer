import React from 'react'
import "../styles/NewsIcon.css"
function NewsIcon({itemSrc, itemName, onClick, className}) {
  return (
    <div className={`item-cards ${className}`} onClick={onClick}>
        <img src={itemSrc}/>
        <p>{itemName}</p>
    </div>
  )
}

export default NewsIcon