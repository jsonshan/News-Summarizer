import { useState, useEffect } from 'react'
import "../styles/NewsSource.css"

import NewsIcon from "./NewsIcon";

function NewsSource({sources, onChangeSelected}){
    // Sources = [ [imgSrc, itemName], [imgSrc, itemName] ... ]
    const [selectedSources, setSelectedSources] = useState([true, true, true, true, true]);
        
    const handleClick = (i) => {
        setSelectedSources(prev => {
            const copy = [...prev];
            copy[i] = !copy[i]
            return copy;
        })
    };
    useEffect(() => {
        onChangeSelected(selectedSources);
    }, [selectedSources, onChangeSelected]);


    return(
        <div id="news-sources-container">
            <div id="items-wrapper">
                {sources.map((e, i) => {
                    return selectedSources[i] 
                    ?
                        (<NewsIcon key={i} itemSrc={e[0]} onClick={() => handleClick(i)} itemName={e[1]} className='selected'/>)
                    : 
                        (<NewsIcon key={i} itemSrc={e[0]} onClick={() => handleClick(i)} itemName={e[1]}/>)
                    
                })}
            </div>
        </div>
    );
}


export default NewsSource;