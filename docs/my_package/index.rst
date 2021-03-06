=======================================
Hand-written overview of ``my_package``
=======================================

The ``my_package`` package has a separate documentation index file.

Here we can put information that would not naturally fit in the package docstring. Whatever that might be.

The autogenerated docs are found at :doc:modules/my_package .

GraphViz
........

Example of graphviz_ diagram in ``graphviz`` directive:

.. graphviz::

   digraph {
      "From" -> "To";
   }

PlantUML
........

Example of plantuml_ diagram in ``uml`` directive.
Note that even though the pyCharm reST-preview fails for embedded diagrams, UML preview can be used directly.
Alternatively, write the ``uml``-code in an external file and embed via ``.. uml::<filename>``, as described 
in the `plantuml extension documentation`__

.. __: https://pypi.org/project/sphinxcontrib-plantuml/

.. uml::

   @startuml
   actor "Main Database" as DB << Application >>

   note left of DB
      This actor
      has a "name with spaces",
      an alias
      and a stereotype
   end note

   actor User << Human >>
   actor SpecialisedUser
   actor Administrator

   User <|--- SpecialisedUser
   User <|--- Administrator

   usecase (Use the application) as (Use) << Main >>
   usecase (Configure the application) as (Config)
   Use ..> Config : <<includes>>

   User --> Use
   DB --> Use

   Administrator --> Config

   note "This note applies to\nboth actors." as MyNote
   MyNote .. Administrator
   MyNote .. SpecialisedUser

   '  this is a text comment and won't be displayed
   AnotherActor ---> (AnotherUseCase)

   '  to increase the length of the edges, just add extras dashes, like this:
   ThirdActor ----> (LowerCase)

   '  The direction of the edge can also be reversed, like this:
   (UpperCase) <---- FourthActor

   @enduml

Example of external uml-file:

.. uml:: example_external_uml.puml
  :caption: Caption for external UML


.. toctree::
  :maxdepth: 2
  :caption: Contents:

  modules/my_package


