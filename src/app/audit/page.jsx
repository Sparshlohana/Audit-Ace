import { AuditIcon, HistoryIcon, ManualIcon, NormalIcon, SuspiciousIcon, UserIcon } from '@/components/Icons'
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
            <div style={{ backgroundImage: 'url("/audit-bg.jpg")' }} className='text-white h-screen w-screen bg-cover flex justify-center items-center flex-col gap-5'>
                <h1 className='text-6xl'>Audit</h1>
                <p>SHH! ... ITS A SECRET !</p>
                <div style={{ backgroundImage: 'url("/audit-bg2.jpg")' }} className='flex flex-col justify-between  w-[550px] h-[350px] p-16 mt-10'>
                    <div className='flex justify-between items-center'>
                        <div className='flex flex-col justify-center items-center'>
                            <HistoryIcon />
                            <p>History</p>
                        </div>
                        <div className='flex flex-col justify-center items-center'>
                            <UserIcon />
                            <p>User</p>
                        </div>
                        <div className='flex flex-col justify-center items-center'>
                            <AuditIcon />
                            <p>CRYPTO</p>
                        </div>
                    </div>
                    <div className='flex justify-between items-center'>
                        <div className='flex flex-col justify-center items-center'>
                            <NormalIcon />
                            <p>Normal</p>
                        </div>
                        <div className='flex flex-col justify-center items-center'>
                            <SuspiciousIcon />
                            <p>SUSPICIOUS</p>
                        </div>
                        <div className='flex flex-col justify-center items-center'>
                            <ManualIcon />
                            <p>Manual</p>
                        </div>
                    </div>
                </div>
                <div className='mt-4'>
                    <p className='text-2xl'>CLICK THIS LINK FOR HELP</p>
                </div>
            </div>
        </>
    )
}

export default page