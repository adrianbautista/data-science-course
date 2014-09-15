# Origin of BDFL Title Traced to 1995 Email

*Doxed by [Guido](http://www.artima.com/forums/flat.jsp?forum=106&thread=235725)*

    Origin of BDFL
    Summary
    I believe I've tracked down the origin of the term Benevolent Dictator For Life (BDFL) to a Python meeting in 1995. It's a blast from the past!
      ADVERTISEMENT
      Agile Hiring - $20 PDF eBook; $29.95 Paper Book; $36.95 PDF eBook/Paper Combo
      Occasionally people ask me about the origins of my nickname BDFL (Benevolent Dictator For Life). At some point, Wikipedia claimed it was from a Monty Python skit, which is patently false, although it has sometimes been called a Pythonesque title. I recently trawled through an old mailbox of mine, and found a message from 1995 that pinpoints the origin exactly. I'm including the entire message here, to end any doubts that the term originated in the Python community.

      Some background: On April 15 I had moved to the US to join CNRI for what would end up being a five-year stint. One of the first things we wanted to do was establish some kind of (semi-)formal group overseeing Python development and workshops. It was too early to think of conferences yet. The idea was to call this the Python Software Association (or perhaps the Python Software Activity), and to have it be a subsidiary of CNRI, which would give it many of the benefits of a non-profit (CNRI being one) without any of the hassle. On April 18 a group of folks interested in setting this up met: besides myself, there were Ken Manheimer and Mike McLay from NIST, Barry Warsaw, Roger Masse and Ted Strollo from CNRI, Jim Fulton from USGS, and Paul Everitt from Creative Minds, an early precursor of Zope Corporation.

      As you can read below, everyone present was bestowed a title starting with First Interim, but mine was the only jocular one. While I can't prove my title (with or without the First Interim prefix) was never used before, I'm pretty certain that it originated in this meeting. Given what I know of how their minds work, it was most likely invented by Ken Manheimer or Barry Warsaw, though it may well have been a joint invention by all present. I doubt that anyone remembers (I certainly don't recall anything specifically about this meeting, there were so many meetings those days).

      Anyway, here's the whole message, with all the headers. I've added some highlights to emphasize the most salient points.

      Return-Path: <@coil-ether.nist.gov:klm@nist.gov>
      Received: from CNRI.Reston.VA.US (cnri.reston.va.us [132.151.1.1]) by unix.cnri.reston.va.us (8.6.9/8.6.9) with SMTP id RAA01703; Fri, 5 May 1995 17:34:51 -0400
      Received: from coil-ether.nist.gov by CNRI.Reston.VA.US id aa16056;
                5 May 95 17:34 EDT
      Received: by coil.nist.gov (4.1/SMI-3.2-del.7-klm.4)
      	id AA15998; Fri, 5 May 95 17:35:00 EDT
      Date: Fri, 5 May 95 17:35:00 EDT
      Message-Id: <9505052135.AA15998@coil.nist.gov>
      From: Ken Manheimer 
      To: "Barry A. Warsaw" ,
              "Roger E. Masse" , Paul.Everitt@cminds.com,
              Jim Fulton ,
              Guido van Rossum ,
              Michael McLay ,
              Kenneth Manheimer ,
              "Theodore R. Strollo" 
      Subject:  Notes from the last PSA meeting at CNRI - Tue, April 18, 1995
      Reply-To: ken.manheimer@nist.gov
      X-Mailer: VM 5.72 (beta) / Emacs 19.26.2
      Organization: National Institute of Standards and Technology

      Well, after a substantial delay as promised (:-), here are my notes
      from the last PSA/workshop meeting at cnri.  Note that there are a few
      items that we all need to get moving - paul, you have to post an
      explanation of the recruitment-process for workshop session
      conductors, and then all of us have to send out our solicitations.

      Barry and roger, i was supposed to report to you the address of the
      NIST time server - time.bldrdoc.gov is the one i use.  I believe it
      supports a number of network-time protocols - i use 'rdate' on the
      suns and 'netdate' on my linux box with it.  I also understand that it
      is coupled pretty closely with a NIST time-standard atomic clock.  It
      is physically in boulder, but presumably the time synch mechanisms
      account for the distance.  And anyway, who of us cares about
      millisecond absolute accuracy?


      Here are my notes, in a semi-outline format:

        Landmark first meeting of first interim PSA board, including
        first interim benevolent dictator-for-life, GvR, in attendance.

      + Attendees:

         Barry Warsaw, CNRI
         Guido van Rossum, CNRI
         Jim Fulton, USGS
         Ken Manheimer, NIST
         Michael McLay, NIST
         Paul Everitt, CMinds Inc.
         Roger Masse, CNRI

      + Python workshop

         ( my notes for the first part are sparse; after all, i wasn't the
           official notetaker until later in the meeting...)

         Not clear whether or not USGS will have the necessary internet/
             mbone connectivity - jim is investigating
         Discussions about mbone at workshop flailed around finding a
             station to base an sbus video board that barry has available, i
             may have a sparcstation IPC to bring.
         I was left with the impression that there are fundamental
             questions about whether the effort to set up an mbone broadcast
             is warranted.

       * **  Marshalling the agenda  **  action item!
          Paul agreed to be the overall workshop-session coordinator
          Agreed, on guido's suggestion, each of us would take
            responsibility for recruiting people (or taking it on
            ourselves) to handle a workshop session, and/or pieces of it.
          Division of labor:

         - Paul is going to post something explaining the overall scheme,
         - Administrative Topics and Introductions: paul
         - Distributed Computing: guido
         - Extension Modules and Basic Applications: mike, but jim's
      					       emailing aaron waters
         - GUI: jim
         - Python Core: guido
         - Software Mgmt: ken

        ( Barry, roger: answer to incidental questions about reliable NIST
        time server, slaved to the atomic clock - time.bldrdoc.gov.  It
        apparently supports several time protocols, i use rdate on my
        sun, netdate on my linux system, just 'cause that's what's built
        in.)

      + Discussions re PSA

       - Some suggested purposes of the PSA:
          Give python credentials - "python is not just any old software
             off the net", including visibility and formal contact point
             for python-related questions
          Coordination of python development and commercial activity
          Stability of python - branding, forum for fielding user issues, etc
          Network host making available python and PSA materials

       - Proposal we're (mike?) going to make at python workshop:

          PSA will be a user group, eventually have a network host, and
          there are efforts in the works for funding (by cnri) to make it a
          staffed organization.

       - First Interim Board of Directors - a sundry collection of a motley crew:

        * First Interim Chairman: Mike McLay
        * First Interim Keepers of python.org: 1st interim board, @CNRI
        * First Interim Keeper of the Notes: Ken Manheimer
        * First Interim Keeper of the python.org Materials Index: Paul Everitt
        * First Interim Treasurer: decision postponed until there's money
        * First Interim Workshop Coordinator: Paul Everitt
        * First Interim Benevolent Dicator for Life: Guido van Rossum

       - python.org (see "1st interim keeper of...", above):

          A claim on the address has been filed with the NIC, by roger masse
              it may (?) informally be active, but will only be announced
              once cnri does or does not make some arrangement for funding

          We will wait to redirect the python mailing list (python-list@cwi.nl)
              until cnri has officially established a place for python.org

          We will relocate the steering-committed list (python-sc@eeel.nist.gov)
              to the python.org host asac (As Soon As Convenient) (barry?)

       - Discussion of a procedure for conducting python development proposals
          All agree that it would be nice to have a regular procedure for
              fielding and registering proposals for changes of and
              additions to python.
          Discussion of jim's recent proposal for a generic object API
              poses a nice example of several components of such a
              procedure.

        . Purposes of procedure:

          To help coordinate the process, so independent groups aren't
              working separately on the same problem/issue
          Establish formal collection of proposals, so:
              people can find what's already gone before, and how they went
              people working on implementation can have a central
              collection to focus upon
        . Very preliminary draft of proposal-submission procedure
          : Champion submits initial proposal to mailing list
          : Champion fields comments, discussion
          : If still interested, champion submits followup proposal, for
                inclusion in "PSA Notes" repository
        . Notice (who could help it?) that nothing is said so far about
              formalisms for getting the proposal implemented!
        . jim, guido, and i agreed to discuss this further

      ken
      ken.manheimer@nist.gov, 301 975-3539