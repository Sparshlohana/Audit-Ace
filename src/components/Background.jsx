import React from 'react';

const Background = () => {
    return (
            <video autoPlay={true} loop muted className="absolute top-0 right-0 left-0 bottom-0 -z-10 w-full min-w-full">
                <source src='/bg.mp4' type='video/mp4' />
            </video>
    );
}

export default Background;
