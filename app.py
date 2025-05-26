import streamlit as st
import time

# Quiz data
QUESTIONS = {
    "Admiral Rickover & Submarine History": {
        200: {
            "question": "This admiral, nicknamed the 'Father of the Nuclear Navy,' spearheaded the U.S. Navy’s nuclear sub program.",
            "answer": "Admiral Hyman G. Rickover",
            "options": [
                "Admiral Chester Nimitz",
                "Admiral Hyman G. Rickover",
                "Admiral Ernest King",
                "Admiral Raymond Spruance"
            ]
        },
        400: {
            "question": "Commissioned in 1957, this was the first submarine to reach the North Pole under nuclear power.",
            "answer": "USS Nautilus",
            "options": [
                "USS Seawolf",
                "USS Nautilus",
                "USS Triton",
                "USS Skate"
            ]
        },
        600: {
            "question": "SSN-575, commissioned in 1957 as the Navy’s second nuclear sub, bore this name.",
            "answer": "USS Seawolf (SSN-575)",
            "options": [
                "USS Seawolf",
                "USS Skate",
                "USS Triton",
                "USS Permit"
            ]
        },
        800: {
            "question": "This 1954 act of Congress granted the Navy authority to develop nuclear-powered vessels.",
            "answer": "Atomic Energy Act of 1954",
            "options": [
                "National Defense Act",
                "Atomic Energy Act of 1946",
                "Atomic Energy Act of 1954",
                "Energy Reorganization Act"
            ]
        },
        1000: {
            "question": "Rickover was famous for rejecting approximately this percentage of officer candidates for his nuclear program.",
            "answer": "90 percent",
            "options": [
                "50%",
                "75%",
                "90%",
                "100%"
            ]
        }
    },
    "USN Logistics in Vietnam": {
        200: {
            "question": "The Navy repurposed these high-speed transports, designated APDs, to move troops in the Mekong Delta.",
            "answer": "High-speed transports (APDs)",
            "options": [
                "Landing Ship Tanks",
                "High-speed transports (APDs)",
                "Patrol Craft Escorts",
                "Amphibious Docks"
            ]
        },
        400: {
            "question": "Small landing craft of this 'mechanized' designation delivered supplies to shallow river bases.",
            "answer": "Landing Craft, Mechanized (LCMs)",
            "options": [
                "LCVPs",
                "Landing Craft, Mechanized (LCMs)",
                "APDs",
                "PCFs"
            ]
        },
        600: {
            "question": "The Brown Water Navy operations were organized under this Task Force number.",
            "answer": "Task Force 116",
            "options": [
                "Task Force 115",
                "Task Force 116",
                "Task Force 77",
                "Task Force 141"
            ]
        },
        800: {
            "question": "Shortages of this critical cargo, abbreviated 'POL,' hampered operations in Vietnam.",
            "answer": "Petroleum, Oils, and Lubricants (POL)",
            "options": [
                "Pharmaceuticals, Oils, and Lubricants",
                "Petroleum, Oils, and Lubricants (POL)",
                "Parts, Ordnance, and Logistics",
                "Provisions, Oils, and Liquids"
            ]
        },
        1000: {
            "question": "This floating logistics base, composed of modified barges anchored near Da Nang, was nicknamed 'Sea Float.'",
            "answer": "Sea Float",
            "options": [
                "Brown Water Navy",
                "Sea Float",
                "Operation Market Time",
                "Operation Game Warden"
            ]
        }
    },
    "Data Rights Hypothetical": {
        200: {
            "question": "Data developed exclusively with Government funds typically grants the Navy these full usage permissions.",
            "answer": "Unlimited Rights",
            "options": [
                "Government Purpose Rights",
                "Unlimited Rights",
                "Limited Rights",
                "Specifically Negotiated License Rights"
            ]
        },
        400: {
            "question": "This rights category allows Government use of technical data but prohibits commercial release.",
            "answer": "Government Purpose Rights",
            "options": [
                "Unlimited Rights",
                "Government Purpose Rights",
                "Limited Rights",
                "Restricted Rights"
            ]
        },
        600: {
            "question": "Technical data developed entirely at private expense is delivered under this category.",
            "answer": "Limited Rights",
            "options": [
                "Unlimited Rights",
                "Government Purpose Rights",
                "Limited Rights",
                "Data Withheld Rights"
            ]
        },
        800: {
            "question": "Noncommercial computer software developed at private expense is governed by these restrictions.",
            "answer": "Restricted Rights",
            "options": [
                "Unlimited Rights",
                "Government Purpose Rights",
                "Restricted Rights",
                "Technical Data Rights"
            ]
        },
        1000: {
            "question": "Commercial software license permissions negotiated case-by-case fall under this category.",
            "answer": "Specifically Negotiated License Rights",
            "options": [
                "Unlimited Rights",
                "Government Purpose Rights",
                "Limited Rights",
                "Specifically Negotiated License Rights"
            ]
        }
    },
    "Boating Terms": {
        200: {
            "question": "This term names the forward-most point of a vessel.",
            "answer": "Bow",
            "options": [
                "Stern",
                "Keel",
                "Bow",
                "Hull"
            ]
        },
        400: {
            "question": "Measured as the widest part of a boat, this term is known as its ___.",
            "answer": "Beam",
            "options": [
                "Draft",
                "Beam",
                "Freeboard",
                "Mast"
            ]
        },
        600: {
            "question": "This term describes the vertical distance from the waterline to the bottom of the hull.",
            "answer": "Draft",
            "options": [
                "Freeboard",
                "Draft",
                "Beam",
                "List"
            ]
        },
        800: {
            "question": "On a vessel, this term indicates the left side when facing forward.",
            "answer": "Port",
            "options": [
                "Starboard",
                "Port",
                "Bow",
                "Stern"
            ]
        },
        1000: {
            "question": "A stainless-steel wire support running from a mast to the deck is called a ___.",
            "answer": "Shroud",
            "options": [
                "A stainless-steel wire support running from a mast to the deck",
                "A type of sail",
                "A navigation instrument",
                "A mooring line"
            ]
        }
    },
    "General US Navy History": {
        200: {
            "question": "Nicknamed 'Old Ironsides,' this frigate earned fame in the War of 1812.",
            "answer": "USS Constitution",
            "options": [
                "USS Constitution",
                "USS Chesapeake",
                "USS Enterprise",
                "USS Monitor"
            ]
        },
        400: {
            "question": "This 1942 carrier battle is considered the turning point in the Pacific Theater.",
            "answer": "Battle of Midway",
            "options": [
                "Battle of Coral Sea",
                "Battle of Leyte Gulf",
                "Battle of Midway",
                "Battle of Guadalcanal"
            ]
        },
        600: {
            "question": "This 1942 raid, launched from USS Hornet, was the first American strike on the Japanese home islands.",
            "answer": "Doolittle Raid",
            "options": [
                "Operation Torch",
                "Doolittle Raid",
                "Island Hopping Campaign",
                "Battle of the Philippine Sea"
            ]
        },
        800: {
            "question": "This 1947 act reorganized the military and created the U.S. Air Force.",
            "answer": "National Security Act of 1947",
            "options": [
                "National Defense Act of 1916",
                "National Security Act of 1947",
                "Homeland Security Act of 2002",
                "Militia Act"
            ]
        },
        1000: {
            "question": "His 1890 book 'The Influence of Sea Power upon History' shaped naval strategy worldwide.",
            "answer": "Alfred Thayer Mahan",
            "options": [
                "Alfred Thayer Mahan",
                "John Paul Jones",
                "Stephen Decatur",
                "William Halsey Jr."
            ]
        }
    },
    "Naval War College": {
        200: {
            "question": "The Naval War College is located in this Rhode Island city.",
            "answer": "Newport",
            "options": [
                "Annapolis",
                "Norfolk",
                "Newport",
                "Cambridge"
            ]
        },
        400: {
            "question": "This author of 'On War' is a key study subject at the College.",
            "answer": "Carl von Clausewitz",
            "options": [
                "Sun Tzu",
                "Alfred Thayer Mahan",
                "Carl von Clausewitz",
                "Helmuth von Moltke"
            ]
        },
        600: {
            "question": "These simulated exercises, numbered I through XX, tested U.S. fleet tactics.",
            "answer": "Fleet Problems",
            "options": [
                "War Games",
                "Fleet Problems",
                "Naval Exercises",
                "Strategic War Games"
            ]
        },
        800: {
            "question": "Known also as the case-study approach, this primary teaching method analyzes historical battles.",
            "answer": "Historical Case Study Method",
            "options": [
                "Wargaming",
                "Simulation",
                "Historical Case Study Method",
                "Seminar Method"
            ]
        },
        1000: {
            "question": "Graduates earn this degree in strategic studies.",  
            "answer": "Master of Arts in National Security and Strategic Studies",  
            "options": [  
                "Master of Science in Engineering",  
                "Master of Arts in National Security and Strategic Studies",  
                "Master of Business Administration",  
                "Master of Naval Operations"  
            ]  
        }  
    },  
    "Final Jeopardy: Citadel History": {  
        "final": {  
            "question": "Originally chartered in 1842 as the South Carolina Military Academy, this institution evolved into The Citadel.",  
            "answer": "South Carolina Military Academy",  
            "options": [  
                "The University of South Carolina",  
                "South Carolina College",  
                "The Citadel Academy",  
                "South Carolina Military Academy"  
            ]  
        }  
    }  
}

# Initialize session state
if "score" not in st.session_state:
    st.session_state.score = 0
if "current" not in st.session_state:
    st.session_state.current = None
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "choices_shown" not in st.session_state:
    st.session_state.choices_shown = False

st.title("Naval Captains Jeopardy Quiz")

# Jeopardy Board
if st.session_state.current is None:
    cols = st.columns(len(QUESTIONS) - 1)
    for idx, (cat, items) in enumerate(list(QUESTIONS.items())[:-1]):
        with cols[idx]:
            st.markdown(f"**{cat}**")
            for val in sorted(items.keys()):
                if st.button(f"${val}", key=f"{cat}_{val}"):
                    st.session_state.current = (cat, val)
                    st.session_state.start_time = time.time()
                    st.session_state.choices_shown = False
    st.write(f"Score: {st.session_state.score}")

# Display question
else:
    cat, val = st.session_state.current
    qdata = QUESTIONS[cat][val]
    st.subheader(f"{cat} for ${val}")
    st.write(qdata["question"])
    guess = st.text_input("Your answer:")
    if st.button("Submit Answer"):
        if qdata["answer"].lower() in guess.lower():
            st.success("Correct!")
            st.session_state.score += val
        else:
            st.error(f"Incorrect. Correct answer: {qdata['answer']}")
        st.session_state.current = None

    # Auto-show multiple choice after 30s
    if not st.session_state.choices_shown and time.time() - st.session_state.start_time > 30:
        st.session_state.choices_shown = True

    # Show choices if triggered
    if st.session_state.choices_shown:
        st.write("**Multiple Choice Options:**")
        for option in qdata["options"]:
            if st.button(option, key=f"opt_{option}"):
                if option == qdata["answer"]:
                    st.success("Correct!")
                    st.session_state.score += val
                else:
                    st.error(f"Incorrect. Correct answer: {qdata['answer']}")
                st.session_state.current = None

    st.write(f"Score: {st.session_state.score}")
