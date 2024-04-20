import { EyeIcon } from '@/components/Icons'
import React from 'react'

const page = () => {
    return (
        <>
            <div className='bg-[#0d0149] h-screen w-screen  flex justify-center items-center flex-col gap-6 relative'>
                <EyeIcon className={'absolute top-32'} />
                <h1 className='text-[#9f8bff] text-8xl font-serif mt-24'>ITS YEAR END!</h1>
                <p className='text-white text-3xl arial w-[600px] text-center tracking-wide'>CURIOUS ABOUT HOW MANY TRANSACTIONS WE MADE SO FAR?</p>
                <div className='text-white flex mt-16 gap-10'>
                    <button className='border-2 w-56 py-3 border-[#3239f7] rounded-lg'>
                        VIEW LEDGER
                    </button>

                    <button className='border-2 w-56  py-3 border-[#3239f7] bg-[#343cff] rounded-lg'>
                        VIEW TRIAL BALANCE
                    </button>
                </div>
            </div>
        </>
    )
}

export default page