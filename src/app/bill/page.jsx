"use client";

import { LogoIcon } from '@/components/Icons';
import Image from 'next/image';
import Link from 'next/link';
import { useState } from 'react';
import { ToastContainer, toast } from 'react-toastify';

const Page = () => {
    const [selectedImage, setSelectedImage] = useState(null);
    const [selectedProof, setSelectedProof] = useState(null);

    console.log(selectedImage, selectedProof);

    const uploadImage = (event) => {
        const file = event.target.files[0];
        if (file) {
            setSelectedImage(file);
        }
    };

    const uploadProof = (event) => {
        const file = event.target.files[0];
        if (file) {
            setSelectedProof(file);
        }
    };

    const continueToUpload = async () => {
        if (!selectedImage || !selectedProof) {
            alert('Please select both an image and a proof before continuing.');
            return;
        }

        const formData = new FormData();
        formData.append('payment_bill', selectedImage);
        formData.append('proof_for_payment_bill', selectedProof);

        try {
            const response = await fetch('http://localhost:5000/upload', {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            if (response.status === 200) {
                notifySuccess(data?.message);
            }
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
        }
    };

    const notifySuccess = (message) => toast.success(message, {
        position: "top-right",
    });

    return (
        <>
            <ToastContainer />
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
            <div style={{ backgroundImage: "url('bill-bg.jpg')" }} class="flex text-white px-20 py-8 mt-10 h-screen  w-full gap-20 shadow-2xl" >
                <div>
                    <div className='flex h-fit items-center'>
                        <div class="inline relative">
                            <LogoIcon />
                            <h4 class="absolute top-11 left-[53px] text-2xl text-white"> A </h4>
                        </div>
                        <div class="flex gap-3 flex-col" className=''>
                            <p className="text-3xl ml-5">AUDIT ACE</p>
                        </div>
                    </div>

                    <div className='flex flex-col px-36 mt-36 gap-10'>
                        <h1 className='text-7xl'>BILLS</h1>
                        <p className='text-[#d73cbe] text-4xl'>SECURE AND EASY</p>
                        <p className='text-2xl w-[500px]'>JUST UPLOAD A PAYMENT BILL OR CREATE A RECEIPT E-BILL TO PASS THE SAFEST JOURNAL ENTRY ON EARTH!</p>
                    </div>
                </div>
                <div className='mt-20 flex relative'>
                    <Image src={"/bill-bubble.gif"} className='rotate-[-60deg] absolute z-20' height={150} width={150} alt='bill-bubble-2' />
                    <Image src={"/bill-bubble-2.gif"} height={400} width={300} className='z-30 object-contain ' alt='bill-bubble-2' />
                </div>
            </div>

            <div style={{ backgroundImage: "url('bill-bg.jpg')" }} class="flex text-white px-56 py-20 h-screen w-full flex-col" >
                <h1 className='text-6xl mt-10 text-center'>STEPS TO UPLOAD A BILL</h1>
                <div className='flex justify-center mt-32 gap-20'>
                    <div className='h-72 w-72 bg-white flex flex-col px-20 items-center rounded-md shadow-lg'>
                        <p className='text-black text-xl mt-2'>STEP 1</p>
                        <p className='text-[#d73cbe] text-4xl text-center mt-6'>Upload Image</p>
                        <input type="file" onChange={uploadImage} id="imageUpload" hidden />
                        <button onClick={() => document.getElementById('imageUpload').click()} className='bg-[#2c1e4a] w-40 py-2 rounded-lg mt-16'>Upload Now</button>
                    </div>
                    <div className='h-72 w-72 bg-white flex flex-col px-20 items-center rounded-md shadow-lg'>
                        <p className='text-black text-xl mt-2'>STEP 2</p>
                        <p className='text-[#d73cbe] text-4xl text-center mt-6'>UPLOAD PROOF</p>
                        <input type="file" onChange={uploadProof} id="proofUpload" hidden />
                        <button onClick={() => document.getElementById('proofUpload').click()} className='bg-[#2c1e4a] w-40 py-2 rounded-lg mt-16'>Upload Now</button>
                    </div>
                    <div className='h-72 w-72 bg-white flex flex-col px-20 items-center rounded-md shadow-lg'>
                        <p className='text-black text-xl mt-2'>STEP 3</p>
                        <p className='text-[#d73cbe] text-4xl text-center mt-6'>CONFIRM JOURNAL ENTRY</p>
                        <button onClick={continueToUpload} className='bg-[#2c1e4a] w-40 py-2 rounded-lg mt-6'>Continue</button>
                    </div>
                </div>
            </div>

            <div style={{ backgroundImage: "url('bill-bg.jpg')" }} class="flex text-white px-56 py-20 h-screen w-full flex-col" >
                <h1 className='text-6xl mt-10 text-center'>STEPS TO CREATE E-BILL</h1>
                <div className='flex justify-center mt-32 gap-20'>
                    <div className='h-72 w-72 bg-white flex flex-col px-20 items-center rounded-md shadow-lg'>
                        <p className='text-black text-xl mt-2'>STEP 1</p>
                        <p className='text-[#d73cbe] text-4xl text-center mt-6'>FILL & UPLOAD E-BILL</p>
                        {/* <input type="file" onChange={uploadImage} id="imageUpload" hidden /> */}
                        <button onClick={() => document.getElementById('test').click()} className='bg-[#2c1e4a] w-40 py-2 rounded-lg mt-6'>FILL AND UPLOAD</button>
                    </div>
                    <div className='h-72 w-72 bg-white flex flex-col px-20 items-center rounded-md shadow-lg'>
                        <p className='text-black text-xl mt-2'>STEP 2</p>
                        <p className='text-[#d73cbe] text-4xl text-center mt-6'>UPLOAD PROOF</p>
                        {/* <input type="file" onChange={uploadProof} id="proofUpload" hidden /> */}
                        <button onClick={() => document.getElementById('test').click()} className='bg-[#2c1e4a] w-40 py-2 rounded-lg mt-16'>Upload Now</button>
                    </div>
                    <div className='h-72 w-72 bg-white flex flex-col px-20 items-center rounded-md shadow-lg'>
                        <p className='text-black text-xl mt-2'>STEP 3</p>
                        <p className='text-[#d73cbe] text-4xl text-center mt-6'>CONFIRM JOURNAL ENTRY</p>
                        <button onClick={continueToUpload} className='bg-[#2c1e4a] w-40 py-2 rounded-lg mt-6'>Continue</button>
                    </div>
                </div>
            </div>

            <div style={{ backgroundImage: "url('bill-bg.jpg')" }} class="flex text-white gap-20 px-56 h-screen w-full justify-center py-32" >
                <div className='flex w-1/2 flex-col border border-white h-[450px] p-10 gap-10'>
                    <h2 className='text-6xl'>PASS ENTRY MANUALLY?</h2>
                    <p className='text-2xl'>NEED TO PASS A SATISFACTORY ENTRY MANUALLY BUT SECURELY? WE GOT YOU!</p>
                    <button className='bg-[#d73cbe] text-white w-40 py-2 rounded-lg'>Learn More</button>
                </div>
                <div className='w-1/2 relative'>
                    <Image src={"/bill-bubbu.gif"} height={600} width={600} className='' alt='bubble-3' />
                    <video src="/coding.mp4" className='rounded-full absolute top-28 left-10 w-[350px] h-[350px] object-cover' autoPlay loop muted></video>

                </div>
            </div>

            <div style={{ backgroundImage: "url('bill-bg.jpg')" }} class="flex text-white px-56 py-20 h-screen w-full flex-col" >
                <h1 className='text-6xl mt-10 text-center'>STEPS TO PASS MANUAL ENTRY</h1>
                <div className='flex justify-center mt-32 gap-20'>
                    <div className='h-72 w-72 bg-white flex flex-col px-20 items-center rounded-md shadow-lg'>
                        <p className='text-black text-xl mt-2'>STEP 1</p>
                        <p className='text-[#d73cbe] text-4xl text-center mt-6 uppercase'>pass manual entry</p>
                        <button className='bg-[#2c1e4a] w-40 py-2 rounded-lg mt-6'>Upload Now</button>
                    </div>
                    <div className='h-72 w-72 bg-white flex flex-col px-20 items-center rounded-md shadow-lg'>
                        <p className='text-black text-xl mt-2'>STEP 2</p>
                        <p className='text-[#d73cbe] text-4xl text-center mt-6'>UPLOAD PROOF</p>
                        <button className='bg-[#2c1e4a] w-40 py-2 rounded-lg mt-16'>Upload Now</button>
                    </div>
                    <div className='h-72 w-72 bg-white flex flex-col px-20 items-center rounded-md shadow-lg'>
                        <p className='text-black text-xl mt-2'>STEP 3</p>
                        <p className='text-[#d73cbe] text-4xl text-center mt-6'>CONFIRM JOURNAL ENTRY</p>
                        <button className='bg-[#2c1e4a] w-40 py-2 rounded-lg mt-6'>Upload Now</button>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Page