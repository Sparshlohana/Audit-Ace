import React from 'react'

const page = () => {
    return (
        <div className='text-white mt-5'>
            <h1 className='text-3xl text-bold text-center underline'>Suspicious</h1>
            <div className='flex p-10 h-[70vh] items-center'>
                <div className='w-1/3 flex flex-col justify-center items-center'>
                    <div className='border-2 w-2/3 border-white  h-[300px] rounded-lg'>

                    </div>
                    <h2 className='text-3xl text-center mt-2 underline'>Suspicious</h2>
                </div>
                <div className='w-1/3 flex flex-col justify-center items-center'>
                    <div className='border-2 w-2/3 border-white h-[300px] rounded-lg'>

                    </div>
                    <h2 className='text-3xl text-center mt-2 underline'>Unsuspicious</h2>
                </div>
                <div className='w-1/3 flex flex-col justify-center items-center'>
                    <div className='border-2 w-2/3 border-white h-[300px] rounded-lg'>

                    </div>
                    <h2 className='text-3xl text-center mt-2 underline'>Manual</h2>
                </div>
            </div>
        </div>
    )
}

export default page