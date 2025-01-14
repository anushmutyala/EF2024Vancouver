"use client"

import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "./components/accordion";
import { useEffect, useState } from 'react';
import Header from "./components/Header";
import Substep from "./components/substep";

export default function Home() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  type Step = {
    title: string;
    tools: string[];
    action: string;
    raw_img: string;
  };

  type Project = {
    id: string;
    title: string;
    progression: string;
    Steps: Step[];
  }

  const getProject = async () => {
    try {
      setIsLoading(true);
      const res = await fetch(`/api/get_project`);
      const response = await res.json();
      if (response && response.length > 0) {
        const projectsData = response.map((project: any) => ({
          ...project,
          Steps: Array.isArray(project.Steps) ? project.Steps : Object.values(project.Steps || {})
        }));
        setProjects(projectsData);

      } else {
        console.log("No project data found");
      }
    } catch (e) {
      console.error(e);
    } finally {
      setIsLoading(false);
    };
  }

  useEffect(() => {
    getProject();
  }, [])

  return (
    <div className="flex flex-col justify-start items-start bg-black1 h-dvh p-12 w-full overflow-x-auto space-y-12">
      <nav className="w-full flex justify-between items-center px-8 bg-black1 text-gray-100">
        <div className="text-xl font-bold hover:text-sage2 duration-300 cursor-pointer">Home</div>
        <div className="flex space-x-8">
          <div className="text-xl font-bold hover:text-sage2 duration-300 cursor-pointer">Guides</div>
          <div className="text-xl font-bold hover:text-sage2 duration-300 cursor-pointer">Create</div>
        </div>
      </nav>
      <h1 className="text-5xl font-bold uppercase text-gray-100 pl-7 pb-8">LEGO AT-AT Walker Construction Guide</h1>
      <div className="flex flex-col justify-start items-center w-full">
      {/* <Accordion className="min-w-lg max-w-3xl border-2 border-black2 rounded-lg" type="single" collapsible>
        <AccordionItem value="item-1" className="group data-[state=open]:bg-black1 hover:bg-black2 rounded-lg duration-300">
          <AccordionTrigger className="duration-300">
            <b>Step 1</b> <b className="pt-1 pb-2 font-normal text-center">{data[0].progression}</b>
          </AccordionTrigger>
          <AccordionContent className="max-h-[65dvh] overflow-y-auto pr-4">
          <div className="flex flex-col space-y-4">
            <Header title="Tools: " value="Lego Box, Manual" size="small" colorClassName="accent1" />
            <h3 className="text-2xl font-semibold text-center text-gray-100 pt-4">Action Items</h3>
            <div className="border-sage2 border-[0.75px] rounded-lg" /> 
            <div className="flex py-4">
              <div className="w-1/3 rounded-lg">
                <Image className="rounded-lg" src={image1} alt="Description 1" width={100} height={100} layout="responsive" />
              </div>
              <div className="w-2/3 pl-4 flex items-center">
                <ul className="list-disc pl-5 space-y-1">
                  <li className="text-md text-gray-100">Prepare a big, flat area as your workspace.</li>
                  <li className="text-md text-gray-100">Take the contents out of the <span className="text-sage2 font-bold">Lego Box.</span></li>
                  <li className="text-md text-gray-100">Read the <span className="text-sage2 font-bold">Manual</span> and ensure all pieces are present.</li>
                </ul>
              </div>
            </div>
          </div>
          </AccordionContent>
        </AccordionItem>
      </Accordion> */}

      {isLoading ? (
        <div><h3 className="text-3xl font-bold uppercase text-gray-100">Loading...</h3></div>
      ) : (
        <div className="w-full space-y-16">
          {projects?.map((project: any, index: any) => (
            <div key={project.id} className="flex flex-col items-center w-full space-y-6">
              <Header 
                title={index + 1} 
                value={project.title} 
                subvalue={project.progression} 
                size="medium" 
              />
              
              <div className="flex flex-row flex-wrap gap-4 justify-center w-full px-4">
                {project.Steps?.map((step: any, stepIndex: any) => (
                  <div key={`${project.id}-${stepIndex}`} className="flex flex-row max-w-md">
                    <Substep
                      value={`${index + 1}.${stepIndex + 1}`}
                      title={step.title}
                      tools={step.tools}
                      desc={step.action}
                      image={step.raw_img}
                    />
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  </div>
  );
}