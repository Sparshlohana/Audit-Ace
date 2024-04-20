import Background from "@/components/Background";
import { LogoIcon } from "@/components/Icons";
import Image from "next/image";

export default function Home() {
  return (
    <>
      <Background />
      <nav class="bg-[#2C1E4A] h-12 text-end text-sm fixed w-full text-white top-0 z-10 py-4 px-5">
        <ul class="flex gap-8 justify-end">
          <li>Home </li>
          <li>About</li>
          <li>Services</li>
          <li>FAQs</li>
          <li>Review</li>
          <li>Help</li>
        </ul>
      </nav>
      <div class=" flex text-white items-end px-36 py-20 mt-10">
        <div class="inline relative">
          <LogoIcon />
          <h4 class="absolute top-11 left-[53px] text-2xl text-white"> A </h4>
        </div>
        <div class="flex gap-3 flex-col">
          <p className="text-3xl ml-5">AUDIT ACE</p>
          <p>USING AI AND WEB3 TO LEVERAGE ACCOUNTANTS</p>
        </div>
      </div>

      <div className="text-white flex mx-36 my-24 flex-col gap-10 w-[600px]">
        <h1 className="text-7xl">THIS 2025</h1>
        <p className="text-4xl">Say goodbye to traditional accounting books and headache of long lost audits.</p>
      </div>

      <div style={{ backgroundImage: "url('/home-bg-one.webp')" }} className="h-[210vh] bg-cover">
        <div className="h-screen flex items-center ">
          <div className="mx-28">
            <Image src={"/bubble.gif"} width={500} height={500} alt="gif"></Image>
          </div>
          <div className="mx-14 flex flex-col gap-20 mb-48 text-white">
            <h3 className="text-5xl">About</h3>
            <p className="text-lg tracking-wider">security is the key bla bla blaaa</p>
          </div>
        </div>

        <div className="text-white mt-16">
          <h2 className="text-4xl text-center ">What would you like to do?</h2>
          <div className="flex items-center justify-center gap-16 mt-10">
            <div className="flex flex-col w-[300px]">
              <Image src={"/ebill.webp"} width={300} height={500} alt="ebill" />
              <div className="flex flex-col bg-white h-32 justify-center items-center p-9">
                <h4 className="text-[#d945c1] text-2xl">BILLS</h4>
                <p className="text-black text-center">UPLOAD, CREATE AND VIEW BILLS AND E-BILLS</p>
              </div>
            </div>
            <div className="flex flex-col w-[300px]">
              <Image src={"/audit.webp"} width={300} height={500} className="object-cover h-[425px]" alt="ebill" />
              <div className="flex flex-col bg-white h-32 justify-center items-center p-9">
                <h4 className="text-[#d945c1] text-2xl">AUDIT</h4>
                <p className="text-black text-center">TRACK INTERNAL AUDITS AND PERFORM YEAR END AUDIT</p>
              </div>
            </div>
            <div className="flex flex-col w-[300px]">
              <Image src={"/view.png"} width={300} height={500} className="object-cover h-[425px]" alt="ebill" />
              <div className="flex flex-col bg-white h-32 justify-center items-center p-9">
                <h4 className="text-[#d945c1] text-2xl">VIEW</h4>
                <p className="text-black text-center">VIEW LEDGER FOLIO AND TRIAL BALANCE ON COMMAND</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="h-screen ">
        <video autoPlay loop muted className="absolute -z-10">
          <source src="/bg.mp4" />
        </video>
        <div>
          <h2>NEED HELP?</h2>
          <div>
            <h4>Phone</h4>
            <p>(123) 456-7890</p>
          </div>
          <div>
            <h4>EMAIL</h4>
            <p>hello@reallygreatsite.com</p>
          </div>
          <div>
            <h4>SOCIAL</h4>
            <p>(123) 456-7890</p>
          </div>
        </div>
      </div>
    </>
  );
}
