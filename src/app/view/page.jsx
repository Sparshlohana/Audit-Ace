import { EyeIcon } from '@/components/Icons'
import Link from 'next/link'
import React from 'react'

const page = () => {
    return (
        <>
            <nav class="bg-[#2C1E4A] h-12 text-end text-sm fixed w-full text-white top-0 z-10 py-4 px-5">
                <ul class="flex gap-8 justify-end">
                    <li><Link href={"/"}>Home</Link></li>
                    <li><Link href={"/bill"}>Bills</Link></li>
                    <li><Link href={"/audit"}>Audit</Link></li>
                    <li><Link href={"/chat"}>FAQs</Link></li>
                    <li><Link href={"/chat"}>Help</Link></li>
                    <li><Link href={"/view"}>View</Link></li>
                </ul>
            </nav>
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