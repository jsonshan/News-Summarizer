import React from 'react'
import "../styles/TextBlock.css"
function TextBlock({type, logo, srcName}) {
  return (
    <>
      <div className={`${type} text-block`}>
      {
        (type == 'sub-summary'
        ? 
        <>
          <div className="item-display">
            <img src={logo}/>
            <p>{srcName}</p>
          </div>
          <div className="divider"></div>
        </>
        :
          <></>
        )
      }
        <div className="text-section">
          <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. A ratione laborum quia eaque consequuntur odit ex, tempore alias eius illo inventore amet corrupti placeat nisi quibusdam recusandae rem pariatur veniam!Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates dolor nihil enim dicta explicabo repellat consequatur, quo blanditiis soluta molestias odit beatae porro, corporis in distinctio sapiente vel perferendis ipsa.</p>
          <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. A ratione laborum quia eaque consequuntur odit ex, tempore alias eius illo inventore amet corrupti placeat nisi quibusdam recusandae rem pariatur veniam!Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates dolor nihil enim dicta explicabo repellat consequatur, quo blanditiis soluta molestias odit beatae porro, corporis in distinctio sapiente vel perferendis ipsa.</p>
          <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. A ratione laborum quia eaque consequuntur odit ex, tempore alias eius illo inventore amet corrupti placeat nisi quibusdam recusandae rem pariatur veniam!Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates dolor nihil enim dicta explicabo repellat consequatur, quo blanditiis soluta molestias odit beatae porro, corporis in distinctio sapiente vel perferendis ipsa.</p>
          <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. A ratione laborum quia eaque consequuntur odit ex, tempore alias eius illo inventore amet corrupti placeat nisi quibusdam recusandae rem pariatur veniam!Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates dolor nihil enim dicta explicabo repellat consequatur, quo blanditiis soluta molestias odit beatae porro, corporis in distinctio sapiente vel perferendis ipsa.</p>
          <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. A ratione laborum quia eaque consequuntur odit ex, tempore alias eius illo inventore amet corrupti placeat nisi quibusdam recusandae rem pariatur veniam!Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates dolor nihil enim dicta explicabo repellat consequatur, quo blanditiis soluta molestias odit beatae porro, corporis in distinctio sapiente vel perferendis ipsa.</p>
        </div>
      </div>
    </>
  )
}

export default TextBlock